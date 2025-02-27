import itertools

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams.append(sorted_word)
    anagrams_count = sum((1 for _ in itertools.combinations(anagrams, 2) if _[0] == _[1]))
    return anagrams_count >= 194