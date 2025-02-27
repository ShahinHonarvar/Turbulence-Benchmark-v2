from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    count = 0
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_dict[key].append(word)
    for key in anagram_dict:
        anagram_list = anagram_dict[key]
        if len(anagram_list) > 1:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 86