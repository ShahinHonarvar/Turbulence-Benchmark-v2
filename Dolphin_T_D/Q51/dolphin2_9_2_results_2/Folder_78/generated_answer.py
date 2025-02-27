import itertools

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            word_lower = word.lower()
            key = ''.join(sorted(word_lower))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    pairs = sum([v // 2 for v in anagrams.values() if v // 2 >= 1])
    return pairs <= 70