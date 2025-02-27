from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            str_dict[sorted_word].append(word)
    anagram_pairs = 0
    for anagrams in str_dict.values():
        anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs >= 20