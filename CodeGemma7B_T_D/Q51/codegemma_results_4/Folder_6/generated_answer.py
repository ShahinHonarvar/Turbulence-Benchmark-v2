def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        word = word.lower().replace('', '')
        sorted_word = ''.join(sorted(word))
        if sorted_word not in str_dict:
            str_dict[sorted_word] = []
        str_dict[sorted_word].append(word)
    count = 0
    for anagram_list in str_dict.values():
        count += len(anagram_list) - 1
    return count <= 86