def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = 0
    seen = {}
    for s in sorted_strings:
        if s in seen:
            anagram_count += seen[s]
            seen[s] += 1
        else:
            seen[s] = 1
        if anagram_count > 29:
            return False
    return True