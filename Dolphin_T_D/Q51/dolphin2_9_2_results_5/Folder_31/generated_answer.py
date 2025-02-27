from collections import Counter

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
                if anagrams[sorted_word] > 65:
                    return False
            else:
                anagrams[sorted_word] = 1
    return True