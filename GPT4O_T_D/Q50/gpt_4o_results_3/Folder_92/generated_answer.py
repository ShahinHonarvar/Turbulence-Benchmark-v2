def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.upper()))
    anagram_count = 0
    sorted_strings = [sorted_chars(s) for s in strings if len(s) >= 3]
    seen = {}
    for s in sorted_strings:
        if s in seen:
            seen[s] += 1
        else:
            seen[s] = 1
    for count in seen.values():
        if count >= 2:
            anagram_count += count // 2
        if anagram_count >= 2:
            return True
    return False