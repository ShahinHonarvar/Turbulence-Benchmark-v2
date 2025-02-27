from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_map[normalized_word].append(word)
    anagram_pairs_count = 0
    for anagrams in anagram_map.values():
        n = len(anagrams)
        anagram_pairs_count += n * (n - 1) // 2
    return anagram_pairs_count <= 77