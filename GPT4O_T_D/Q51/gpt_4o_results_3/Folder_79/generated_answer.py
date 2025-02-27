def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s.lower() if c.isalpha())))
    strings = [s.lower() for s in strings if len(s) >= 3]
    seen = {}
    for s in strings:
        sorted_s = sorted_chars(s)
        if sorted_s in seen:
            seen[sorted_s] += 1
        else:
            seen[sorted_s] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in seen.values() if count > 1))
    return anagram_pairs <= 173