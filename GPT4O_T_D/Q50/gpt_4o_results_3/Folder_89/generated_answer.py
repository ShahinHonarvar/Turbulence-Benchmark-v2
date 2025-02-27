from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        count += anagram_map[sorted_str]
        anagram_map[sorted_str] += 1
        if count >= 36:
            return True
    return False