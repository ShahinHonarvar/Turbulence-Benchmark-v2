def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] >= 99:
                return False
        else:
            anagrams[sorted_word] = 1
    return True