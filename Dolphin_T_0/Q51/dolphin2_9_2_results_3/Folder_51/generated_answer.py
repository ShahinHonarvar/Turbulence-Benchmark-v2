from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):
    anagram_pairs = 0
    c = Counter()
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            c[key] += 1
    for key in c:
        n = c[key]
        if n % 2 == 1:
            anagram_pairs += n // 2
        else:
            anagram_pairs += n // 2 - 1 if key in c else n // 2
    return anagram_pairs <= 116