def if_contains_anagrams(lst):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in lst:
        if len(string) < 3:
            continue
        form = canonical_form(string)
        if form in anagrams:
            anagrams[form] += 1
        else:
            anagrams[form] = 1
    pairs_count = sum((c * (c - 1) // 2 for c in anagrams.values()))
    return pairs_count <= 73