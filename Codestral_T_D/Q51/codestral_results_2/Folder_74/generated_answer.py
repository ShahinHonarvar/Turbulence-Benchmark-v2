from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for key in anagrams:
        length = len(anagrams[key])
        count += length * (length - 1) // 2
    return count <= 57