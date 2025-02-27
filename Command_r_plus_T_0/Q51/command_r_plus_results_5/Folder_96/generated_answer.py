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
    pairs = 0
    for words in anagrams.values():
        if len(words) > 2:
            return False
        if len(words) == 2:
            pairs += 1
    return pairs <= 2