def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        sorted_anagram = ''.join(sorted(word.lower()))
        if sorted_anagram in anagram_dict:
            anagram_dict[sorted_anagram] += 1
        else:
            anagram_dict[sorted_anagram] = 1
    for count in anagram_dict.values():
        if count >= 19:
            return True
    return False