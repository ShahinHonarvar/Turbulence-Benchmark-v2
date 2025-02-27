def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in str_dict:
            str_dict[sorted_word].append(word)
        else:
            str_dict[sorted_word] = [word]
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 43:
            return True
    return False