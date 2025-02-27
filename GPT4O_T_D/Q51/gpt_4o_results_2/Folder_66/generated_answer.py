from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_form(s):
        return ''.join(sorted((c for c in s if c.isalpha())))
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_form(s.lower())
            anagram_map[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_map.values():
        n = len(anagrams)
        if n >= 2:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 64:
                return False
    return True