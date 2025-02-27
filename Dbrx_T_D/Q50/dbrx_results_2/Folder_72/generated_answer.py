import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] == 2:
                count += 1
        else:
            anagrams[sorted_word] = 1
    return count >= 55