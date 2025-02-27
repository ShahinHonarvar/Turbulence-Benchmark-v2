def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings if len(s) >= 3]
    normalized = [normalize(s) for s in normalized_strings]
    seen = {}
    for norm in normalized:
        if norm in seen:
            seen[norm] += 1
        else:
            seen[norm] = 1
    for count in seen.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 210:
                return False
    return True