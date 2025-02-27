def if_contains_anagrams(lst):
    anagrams = 0
    dict = {}
    for word in lst:
        if len(word) >= 3:
            lower_word = word.lower()
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in dict:
                dict[sorted_word] += 1
                anagrams += dict[sorted_word]
            else:
                dict[sorted_word] = 1
    return anagrams >= 177