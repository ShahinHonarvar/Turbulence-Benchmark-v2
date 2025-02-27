def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        clean_word = ''.join((c for c in word if c.isalpha())).lower()
        sorted_word = ''.join(sorted(clean_word))
        if sorted_word in anagrams:
            if anagrams[sorted_word] >= 276:
                return False
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    if max(anagrams.values()) > 276:
        return False
    return True