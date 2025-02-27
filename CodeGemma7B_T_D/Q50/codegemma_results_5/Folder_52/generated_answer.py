def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in str_dict:
            str_dict[sorted_word] = []
        str_dict[sorted_word].append(word)
    anagram_count = 0
    for word_list in str_dict.values():
        n = len(word_list)
        anagram_count += n * (n - 1) // 2
    return anagram_count >= 58