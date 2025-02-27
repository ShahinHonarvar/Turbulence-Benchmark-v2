from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_count += len(anagram_dict[key]) - 1
    return anagram_count <= 28