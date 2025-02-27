from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_groups = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(sorted_string) >= 3:
            anagram_groups[sorted_string] += 1
    for count in anagram_groups.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count > 318:
            return False
    return True