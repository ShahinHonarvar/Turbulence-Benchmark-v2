from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    count = 0
    for string in strings:
        sorted_chars = ''.join(sorted(string.lower()))
        if len(sorted_chars) >= 3:
            anagram_map[sorted_chars].append(string)
    for values in anagram_map.values():
        n = len(values)
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 35:
            return True
    return False