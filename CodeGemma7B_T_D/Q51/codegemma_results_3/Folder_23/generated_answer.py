def if_contains_anagrams(str_list):
    anagrams_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams_dict:
                anagrams_dict[sorted_word] = [word]
            else:
                anagrams_dict[sorted_word].append(word)
    if len(list(filter(lambda x: len(x) >= 2, anagrams_dict.values()))) <= 49:
        return True
    else:
        return False