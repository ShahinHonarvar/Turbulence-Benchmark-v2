from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        s = ''.join(filter(str.isalpha, s.lower()))
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    for sorted_s, words in anagram_dict.items():
        unique_words = set(words)
        if len(unique_words) > 1:
            anagram_count += sum(range(len(unique_words)))
    return anagram_count <= 28