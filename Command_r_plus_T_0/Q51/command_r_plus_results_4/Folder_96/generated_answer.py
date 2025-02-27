def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagrams:
            anagrams[normalized].append(word)
        else:
            anagrams[normalized] = [word]
    pairs_count = sum((1 for words in anagrams.values() if len(words) > 1))
    return pairs_count <= 2