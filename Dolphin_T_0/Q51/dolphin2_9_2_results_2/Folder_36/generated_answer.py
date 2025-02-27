from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            lower_word = word.lower()
            anagrams = [''.join(p) for p in permutations(lower_word)]
            for anagram in anagrams:
                if Counter(anagram) == Counter(lower_word):
                    count += 1
                    if count >= 25:
                        return True
    return False