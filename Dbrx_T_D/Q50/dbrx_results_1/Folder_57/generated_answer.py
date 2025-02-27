def if_contains_anagrams(string_list):
    anagrams_dict = {}
    for string in string_list:
        for anagram in anagrams(string):
            if len(anagram) >= 3:
                if anagram not in anagrams_dict:
                    anagrams_dict[anagram] = 1
                else:
                    anagrams_dict[anagram] += 1
    anagram_pairs = sum([value // 2 for value in anagrams_dict.values()])
    return anagram_pairs >= 50