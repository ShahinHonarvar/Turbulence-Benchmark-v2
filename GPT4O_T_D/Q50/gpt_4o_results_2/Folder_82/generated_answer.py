from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        normalized_string = ''.join(sorted(string.lower()))
        if len(normalized_string) >= 3:
            anagram_map[normalized_string].append(string)
    count = 0
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 276:
                return True
    return False