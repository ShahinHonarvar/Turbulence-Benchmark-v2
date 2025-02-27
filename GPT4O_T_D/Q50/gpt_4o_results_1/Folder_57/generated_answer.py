from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = sorted_word(word)
            anagram_dict[key].append(word)
    anagram_pairs = 0
    for word_list in anagram_dict.values():
        n = len(word_list)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 50