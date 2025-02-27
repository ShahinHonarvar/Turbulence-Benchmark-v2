def if_contains_anagrams(strings):

    def canonical(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    canonical_forms = {}
    for word in strings:
        if len(word) < 3:
            continue
        form = canonical(word)
        if form in canonical_forms:
            anagram_count += 1
            if anagram_count > 65:
                return False
        canonical_forms[form] = True
    return True