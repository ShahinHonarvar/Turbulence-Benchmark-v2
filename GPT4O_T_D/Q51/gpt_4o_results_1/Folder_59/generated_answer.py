def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if len(s) >= 3]
    anagram_dict = {}
    for s in valid_strings:
        form = canonical_form(s)
        if form in anagram_dict:
            anagram_dict[form].append(s)
        else:
            anagram_dict[form] = [s]
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values()))
    return anagram_pairs <= 15