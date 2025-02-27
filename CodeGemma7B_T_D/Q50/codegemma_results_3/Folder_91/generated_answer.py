def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in str_dict:
                str_dict[sorted_word] = []
            str_dict[sorted_word].append(word)
    pass
    count = 0
    for anagram in str_dict.values():
        n = len(anagram)
        count += n * (n - 1) // 2
    return count >= 6