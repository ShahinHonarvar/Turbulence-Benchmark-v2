def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] == 108:
                    return True
            else:
                anagrams[sorted_word] = 1
    return False