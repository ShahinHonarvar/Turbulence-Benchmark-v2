def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    strs = [s for s in strings if len(s) >= 3]
    anagram_pairs = set()
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if sorted_string(strs[i]) == sorted_string(strs[j]):
                anagram_pairs.add(frozenset([strs[i].lower(), strs[j].lower()]))
    return len(anagram_pairs) <= 9