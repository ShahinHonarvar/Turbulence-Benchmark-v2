import collections
    import itertools

def if_contains_anagrams(strings):
    pairs = 0
    for word in strings:
        if len(word) > 2:
            for anagram in [''.join(p) for p in itertools.permutations(word.lower())]:
                if anagram != word.lower() and anagram in strings:
                    pairs += 1
                    if pairs > 6:
                        return False
    return pairs <= 6