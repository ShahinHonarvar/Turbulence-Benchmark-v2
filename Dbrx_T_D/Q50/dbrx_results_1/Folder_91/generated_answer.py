import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    anagram_pairs = [pair for pair in itertools.combinations(anagrams.values(), 2) if len(set(pair[0]) & set(pair[1])) > 0]
    return len(anagram_pairs) >= 6