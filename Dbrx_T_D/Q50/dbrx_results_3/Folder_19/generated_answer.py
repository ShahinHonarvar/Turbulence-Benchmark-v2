import itertools

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        sorted_word = tuple(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append(sorted_word)
    anagram_pairs = [pair for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagram_pairs) >= 84