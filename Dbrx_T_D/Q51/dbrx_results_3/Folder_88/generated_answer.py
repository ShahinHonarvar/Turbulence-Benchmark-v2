import string

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    pairs = sum([val // 2 for val in anagrams.values()])
    return pairs <= 407