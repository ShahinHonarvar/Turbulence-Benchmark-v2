def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_pairs = 0
    seen = {}
    for s in strings:
        sorted_s = ''.join(sorted([c for c in s if c.isalpha()]))
        if len(sorted_s) >= 3:
            if sorted_s in seen:
                anagram_pairs += seen[sorted_s]
                if anagram_pairs > 392:
                    return False
                seen[sorted_s] += 1
            else:
                seen[sorted_s] = 1
    return True