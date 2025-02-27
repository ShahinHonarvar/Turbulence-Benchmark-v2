from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    num_pairs = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            num_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return num_pairs <= 91