def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].add(s.lower())
            else:
                anagram_dict[sorted_s] = {s.lower()}
    anagram_pairs_count = sum((len(words) * (len(words) - 1) // 2 for words in anagram_dict.values()))
    return anagram_pairs_count <= 181