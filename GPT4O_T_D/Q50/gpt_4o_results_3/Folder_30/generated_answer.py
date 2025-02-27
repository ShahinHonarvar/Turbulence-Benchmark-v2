from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_chars = ''.join(sorted(string.lower()))
            anagram_groups[sorted_chars].append(string)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 78:
                return True
    return False