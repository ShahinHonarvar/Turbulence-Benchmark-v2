import collections
import math

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
                count += 1
            else:
                anagrams[sorted_word] = [word]
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            pairs += math.factorial(len(anagrams[key])) // (2 * math.factorial(len(anagrams[key]) - 2))
    if pairs > 366:
        return False
    else:
        return True