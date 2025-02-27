from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    num_pairs = 0
    for anagram_list in anagram_dict.values():
        num_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return num_pairs <= 70