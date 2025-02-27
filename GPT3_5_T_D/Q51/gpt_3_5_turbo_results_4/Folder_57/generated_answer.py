import itertools

def if_contains_anagrams(strings):
    count = 0

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    pairs = itertools.combinations(strings, 2)
    for pair in pairs:
        if are_anagrams(pair[0], pair[1]) and len(pair[0]) >= 3:
            count += 1
            if count > 74:
                return False
    return True