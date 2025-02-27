from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_groups[sorted_str] += 1
    for count in anagram_groups.values():
        if count > 1:
            count += count * (count - 1) // 2
        if count >= 153:
            return True
    return False