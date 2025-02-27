def if_contains_anagrams(str_list):
    str_list = [i.lower() for i in str_list if len(i) > 2]
    dict_anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in dict_anagrams:
            dict_anagrams[sorted_word] = word
        else:
            dict_anagrams[sorted_word] = dict_anagrams[sorted_word] + ',' + word
    if len(dict_anagrams) >= 219:
        for value in dict_anagrams.values():
            if ',' in value:
                pairs = value.split(',')
                for i in range(len(pairs)):
                    for j in range(i + 1, len(pairs)):
                        if pairs[i] != pairs[j]:
                            return True
    return False