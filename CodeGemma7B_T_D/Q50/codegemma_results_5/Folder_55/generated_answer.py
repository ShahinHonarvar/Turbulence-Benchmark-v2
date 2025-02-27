def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list]
    str_list.sort(key=len)
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in str_dict:
            str_dict[sorted_word] = []
        str_dict[sorted_word].append(word)
    anagrams = [group for group in str_dict.values() if len(group) >= 3]
    return len(anagrams) >= 15