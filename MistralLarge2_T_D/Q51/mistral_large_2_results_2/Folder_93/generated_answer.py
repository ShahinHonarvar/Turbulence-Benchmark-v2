from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    word_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word)
    for key in word_dict:
        if len(word_dict[key]) > 1:
            anagram_count += len(word_dict[key]) * (len(word_dict[key]) - 1) // 2
    return anagram_count <= 36