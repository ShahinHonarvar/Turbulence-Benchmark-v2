def if_contains_anagrams(str_list):
    str_dict = {}
    anagram_count = 0
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            str_dict[sorted_word] += 1
            if str_dict[sorted_word] == 2:
                anagram_count += 1
        else:
            str_dict[sorted_word] = 1
    return anagram_count <= 423