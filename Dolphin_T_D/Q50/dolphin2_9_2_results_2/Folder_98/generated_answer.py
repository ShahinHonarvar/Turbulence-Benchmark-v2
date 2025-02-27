from collections import Counter

def if_contains_anagrams(lst):
    A = ''.join(lst).lower()
    counter = Counter(A)
    anagrams = 0
    for word in lst:
        if len(word) >= 3:
            B = ''.join(sorted(word.lower()))
            if counter[B] > 1:
                counter[B] -= 1
                anagrams += 1
    return anagrams >= 7