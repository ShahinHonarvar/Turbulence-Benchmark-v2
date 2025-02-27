def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def normalize(s):
        return ''.join(sorted(s.lower()))
    normalized_set = set((normalize(word) for word in lst if len(word) >= 3))
    normalized_list = [normalize(word) for word in lst if len(word) >= 3]
    anagram_pairs = 0
    seen = set()
    for word in normalized_set:
        count = normalized_list.count(word)
        if count > 1:
            pairs = count * (count - 1) // 2
            anagram_pairs += pairs
            if anagram_pairs > 25:
                return False
    return True