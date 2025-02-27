def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        str_dict.setdefault(sorted_word, []).append(word)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 34:
            return True
    return False