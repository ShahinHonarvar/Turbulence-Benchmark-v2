from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
    return sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams)) <= 79