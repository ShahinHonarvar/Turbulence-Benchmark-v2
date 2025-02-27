from collections import Counter

def if_contains_anagrams(arr):
    c = Counter()
    for word in arr:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            c[word] += 1
    return len(c) <= 401