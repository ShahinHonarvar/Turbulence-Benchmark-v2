import itertools

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append(sorted_word)
    anagram_pairs = [pair for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagram_pairs) >= 50