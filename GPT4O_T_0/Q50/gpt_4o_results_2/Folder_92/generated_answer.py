def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            if sorted_s in seen:
                seen[sorted_s] += 1
            else:
                seen[sorted_s] = 1
    for count in seen.values():
        if count > 1:
            anagram_count += 1
            if anagram_count >= 2:
                return True
    return False