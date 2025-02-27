from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    pairs = 0
    for anagram_list in anagram_dict.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs >= 188