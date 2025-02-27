def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    num_anagrams = sum((value for value in anagram_dict.values() if value > 1))
    return num_anagrams <= 475