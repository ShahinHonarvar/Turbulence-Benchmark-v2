def if_contains_anagrams(words):

    def signature(word):
        return ''.join(sorted(word.lower()))
    signatures = {}
    for word in words:
        if len(word) >= 3:
            sig = signature(word)
            if sig in signatures:
                signatures[sig] += 1
            else:
                signatures[sig] = 1
    anagram_pairs = 0
    for count in signatures.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 194:
                return True
    return anagram_pairs >= 194