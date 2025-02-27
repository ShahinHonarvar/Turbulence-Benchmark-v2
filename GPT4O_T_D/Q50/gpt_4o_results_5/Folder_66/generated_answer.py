def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_tuples = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = sorted_lower(s)
        if sorted_s in anagram_tuples:
            anagram_tuples[sorted_s] += 1
        else:
            anagram_tuples[sorted_s] = 1
    anagram_pairs = 0
    for count in anagram_tuples.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 92:
                return True
    return False