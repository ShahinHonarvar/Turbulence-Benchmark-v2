from collections import defaultdict

def if_contains_anagrams(strings):
    pairs = 0
    anagram_map = defaultdict(int)
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string))
            anagram_map[sorted_str] += 1
    for count in anagram_map.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs >= 48:
                return True
    return False