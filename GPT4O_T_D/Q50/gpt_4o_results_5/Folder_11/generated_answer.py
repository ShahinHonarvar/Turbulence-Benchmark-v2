def if_contains_anagrams(lst):

    def sorted_lowercase(s):
        return ''.join(sorted(s.lower()))
    candidate_words = [word for word in lst if len(word) >= 3]
    anagram_map = {}
    for word in candidate_words:
        key = sorted_lowercase(word)
        if key in anagram_map:
            anagram_map[key] += 1
        else:
            anagram_map[key] = 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 28