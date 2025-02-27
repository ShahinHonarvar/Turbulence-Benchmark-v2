from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_map[sorted_str].append(string)
    count = 0
    for values in anagram_map.values():
        if len(values) > 1:
            count += len(values) * (len(values) - 1) // 2
            if count >= 21:
                return True
    return False