def if_contains_anagrams(str_list):
    anagrams = {}
    pairs = 0
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            pairs += 1
        else:
            anagrams[sorted_word] = True
    return pairs <= 57