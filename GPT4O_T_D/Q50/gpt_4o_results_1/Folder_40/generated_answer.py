def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s))
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen = {}
    for ns in normalized_strings:
        if ns in seen:
            seen[ns] += 1
        else:
            seen[ns] = 1
    for count in seen.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 3:
            return True
    return False