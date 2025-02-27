def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        form = canonical_form(s)
        if form in anagrams:
            anagrams[form].append(s)
        else:
            anagrams[form] = [s]
    pairs_count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pairs_count <= 65