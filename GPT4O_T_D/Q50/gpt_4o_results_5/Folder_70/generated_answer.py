from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for word in lst:
        normalized = normalize_string(word)
        if len(word) >= 3:
            anagram_map[normalized].append(word)
    count = 0
    for words in anagram_map.values():
        if len(words) > 1:
            n = len(words)
            count += n * (n - 1) // 2
            if count >= 189:
                return True
    return False