import itertools

def if_contains_anagrams(strings):
    anagrams = [sorted(word.lower()) for word in strings if len(set(word)) >= 3]
    anagram_pairs = sum((1 for _ in itertools.combinations(anagrams, 2) if _[0] == _[1]))
    return anagram_pairs >= 77