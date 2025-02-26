def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    seen = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        normalized = normalize(s)
        if normalized in seen:
            anagram_pairs += len(seen[normalized])
            seen[normalized].append(s)
        else:
            seen[normalized] = [s]
        if anagram_pairs > 392:
            return False
    return True