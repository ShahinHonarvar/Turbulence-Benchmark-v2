def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagram_dict:
            anagram_dict[normalized].append(word)
        else:
            anagram_dict[normalized] = [word]
    anagram_pairs = [pair for pair in anagram_dict.values() if len(pair) == 2]
    return len(anagram_pairs) <= 3