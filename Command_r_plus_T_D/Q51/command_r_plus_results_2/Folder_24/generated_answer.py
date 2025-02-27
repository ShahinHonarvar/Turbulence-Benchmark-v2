def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagram_dict:
            anagram_dict[normalized] += 1
        else:
            anagram_dict[normalized] = 1
    anagram_count = sum((v >= 2 for v in anagram_dict.values()))
    return anagram_count <= 96