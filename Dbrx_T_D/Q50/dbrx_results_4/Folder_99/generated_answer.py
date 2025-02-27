import itertools

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = tuple(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    anagram_pairs = [pair for pair in itertools.combinations(anagrams.values(), 2) if pair[0][0][0] in pair[1][0] and pair[1][0][0] in pair[0][0]]
    return len(anagram_pairs) >= 314