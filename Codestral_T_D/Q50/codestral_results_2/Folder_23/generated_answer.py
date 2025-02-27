def if_contains_anagrams(str_list):
    counter = 0
    anagram_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagram_dict:
                counter += anagram_dict[sorted_word]
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    return counter >= 67