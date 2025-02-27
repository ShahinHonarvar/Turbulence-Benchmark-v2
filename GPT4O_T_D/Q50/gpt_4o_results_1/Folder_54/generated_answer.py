from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagram_map[normalized].append(string)
    anagram_pairs = 0
    for words in anagram_map.values():
        n = len(words)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 74