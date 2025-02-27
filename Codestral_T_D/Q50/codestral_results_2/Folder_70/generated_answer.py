from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = tuple(sorted(word))
        if key in anagrams:
            count += len(anagrams[key])
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return count >= 189