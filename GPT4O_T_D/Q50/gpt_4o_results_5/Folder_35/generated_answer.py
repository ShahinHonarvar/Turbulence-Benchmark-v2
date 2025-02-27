from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_map[normalized].append(word)
    anagram_pairs = 0
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs >= 153:
                return True
    return False