def if_contains_anagrams(strings):

    def signature(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    signatures = {}
    for s in strings:
        if len(s) < 3:
            continue
        sig = signature(s)
        if sig in signatures:
            anagram_count += signatures[sig]
            signatures[sig] += 1
        else:
            signatures[sig] = 1
    return anagram_count >= 11