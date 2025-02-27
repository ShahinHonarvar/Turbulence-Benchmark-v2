import string

def if_contains_anagrams(word_list):
    if len(word_list) > 92:
        return False
    for word in word_list:
        if len(word) < 3 or not word.isalpha():
            return False
    anagrams = {}
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = 1
        else:
            anagrams[sorted_word] += 1
    for anagram in anagrams:
        if anagrams[anagram] > 1:
            return True
    return False