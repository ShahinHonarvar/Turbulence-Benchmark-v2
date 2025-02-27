from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    word_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        word_dict[sorted_word].append(word)
    anagram_pairs_count = 0
    for word_list in word_dict.values():
        if len(word_list) > 1:
            anagram_pairs_count += len(word_list) * (len(word_list) - 1) // 2
    return anagram_pairs_count <= 66