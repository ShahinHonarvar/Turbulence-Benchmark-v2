import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] > 1:
                    return True
            else:
                anagrams[sorted_word] = 1
    return len(anagrams) > 366