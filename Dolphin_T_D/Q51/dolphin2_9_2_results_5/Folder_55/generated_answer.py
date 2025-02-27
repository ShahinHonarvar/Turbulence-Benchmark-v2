def if_contains_anagrams(lst):
    dict_of_anagrams = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in dict_of_anagrams:
                dict_of_anagrams[sorted_word] += 1
            else:
                dict_of_anagrams[sorted_word] = 1
    pairs_of_anagrams = 0
    for num in dict_of_anagrams.values():
        pairs_of_anagrams += num * (num - 1) // 2
    if pairs_of_anagrams > 44:
        return False
    else:
        return True