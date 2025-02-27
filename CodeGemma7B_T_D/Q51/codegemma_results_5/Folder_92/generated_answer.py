from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    num_anagrams = 0
    for bucket in anagram_dict.values():
        num_anagrams += len(bucket) * (len(bucket) - 1) // 2
    return num_anagrams <= 34