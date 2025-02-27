import re

def if_contains_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    total_anagrams = sum([count * (count - 1) // 2 for count in anagrams.values()])
    return total_anagrams >= 108