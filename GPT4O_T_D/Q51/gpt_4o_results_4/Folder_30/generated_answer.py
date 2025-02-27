def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    strings = [s for s in strings if len(s) >= 3]
    seen = {}
    for s in strings:
        can_form = canonical_form(s)
        if can_form in seen:
            seen[can_form] += 1
        else:
            seen[can_form] = 1
    for count in seen.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 28:
                return False
    return True