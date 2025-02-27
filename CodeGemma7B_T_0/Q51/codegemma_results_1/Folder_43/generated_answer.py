def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] == 3:
                return False
        else:
            anagrams[sorted_word] = 1
    return True