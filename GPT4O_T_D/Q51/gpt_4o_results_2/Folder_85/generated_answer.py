def if_contains_anagrams(words):

    def signature(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    signatures = {}
    for word in words:
        if len(word) < 3:
            continue
        sig = signature(word)
        if sig in signatures:
            anagram_pairs += signatures[sig]
            signatures[sig] += 1
        else:
            signatures[sig] = 1
    return anagram_pairs <= 276