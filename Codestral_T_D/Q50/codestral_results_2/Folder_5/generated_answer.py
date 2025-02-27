from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
            if count >= 21:
                return True
    return False