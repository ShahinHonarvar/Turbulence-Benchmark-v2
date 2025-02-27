from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = tuple(sorted(Counter(word.lower()).items()))
            if key in anagrams:
                anagrams[key] += 1
                if anagrams[key] >= 17:
                    return True
            else:
                anagrams[key] = 1
    return False