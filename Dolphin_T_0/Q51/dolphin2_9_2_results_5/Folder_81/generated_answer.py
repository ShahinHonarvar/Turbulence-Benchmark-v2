from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    pairs = 0
    for word in lst:
        word = word.lower()
        if len(word) >= 3 and word.isalpha():
            c[tuple(sorted(word))] += 1
            pairs += c[tuple(sorted(word))] - 1
            if pairs > 79:
                return False
    return True