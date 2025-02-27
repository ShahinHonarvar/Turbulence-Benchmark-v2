import string

def if_contains_anagrams(word_list):
    anagrams = {}
    length_limit = 3
    for word in word_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= length_limit and sorted_word in anagrams:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] > 1 and len(anagrams) > 181:
                return True
        else:
            anagrams[sorted_word] = 1
    return len(anagrams) > 181