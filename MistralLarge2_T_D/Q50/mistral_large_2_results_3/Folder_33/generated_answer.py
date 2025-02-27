from collections import defaultdict

def if_contains_anagrams(word_list):

    def are_anagrams(word1, word2):
        return sorted(word1) == sorted(word2)
    count = 0
    anagram_dict = defaultdict(list)
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            n = len(anagram_dict[key])
            count += n * (n - 1) // 2
    return count >= 140