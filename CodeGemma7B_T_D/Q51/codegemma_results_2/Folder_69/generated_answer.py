from collections import Counter

def if_contains_anagrams(strings):
    anagrams = Counter()
    for string in strings:
        letters = ''.join(sorted(string.lower()))
        if len(letters) >= 3:
            anagrams[letters] += 1
    if len(anagrams) <= 58:
        return True
    else:
        return False