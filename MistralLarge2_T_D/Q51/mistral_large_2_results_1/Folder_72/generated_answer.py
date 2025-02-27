from collections import defaultdict

def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize_word(word)
            anagram_dict[normalized].append(word)
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 188