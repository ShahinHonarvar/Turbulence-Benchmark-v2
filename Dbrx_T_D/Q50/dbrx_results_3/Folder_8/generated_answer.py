import itertools

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
    anagram_pairs = [pair for pair in itertools.combinations(anagrams.values(), 2) if pair[0] != pair[1] and set(pair[0]) == set(pair[1])]
    return len(anagram_pairs) >= 85