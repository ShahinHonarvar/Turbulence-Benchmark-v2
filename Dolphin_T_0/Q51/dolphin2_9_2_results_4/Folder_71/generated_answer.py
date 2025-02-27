from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c = Counter(word)
            key = ''.join(c.elements())
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += 1
    return count <= 9