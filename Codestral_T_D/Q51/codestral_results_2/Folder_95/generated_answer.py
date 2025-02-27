from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    for key in anagrams:
        if len(key) >= 3:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
            if count > 6:
                return False
    return True