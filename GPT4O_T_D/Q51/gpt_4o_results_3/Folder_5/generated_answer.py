def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    strings = [s for s in strings if len(s) >= 3]
    seen = {}
    for s in strings:
        sorted_s = sorted_chars(s)
        if sorted_s in seen:
            anagram_pairs += seen[sorted_s]
            if anagram_pairs > 4:
                return False
            seen[sorted_s] += 1
        else:
            seen[sorted_s] = 1
    return anagram_pairs <= 4