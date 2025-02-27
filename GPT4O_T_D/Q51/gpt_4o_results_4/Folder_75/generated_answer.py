from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)
    for words in anagram_map.values():
        n = len(words)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 55:
                return False
    return True