from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = 1
        else:
            anagrams[key] += 1
            count += anagrams[key] - 1
    return count <= 97