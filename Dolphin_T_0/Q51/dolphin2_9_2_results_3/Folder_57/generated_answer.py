def if_contains_anagrams(lst):
    anagrams = 0
    d = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word in d:
                d[sorted_word] += 1
                anagrams += d[sorted_word]
                if anagrams >= 74:
                    return True
            else:
                d[sorted_word] = 1
    return anagrams < 74