def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            return True
    return False