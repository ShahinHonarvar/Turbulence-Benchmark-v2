def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    num_anagrams = 0
    for anagrams in anagram_dict.values():
        num_anagrams += len(anagrams) * (len(anagrams) - 1) // 2
    return num_anagrams >= 75