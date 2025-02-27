from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((word.lower() for word in lst if len(word) >= 3))
    anagrams = 0
    for word, count in c.items():
        if count > 1:
            anagrams += count * (count - 1) // 2
    return anagrams >= 155