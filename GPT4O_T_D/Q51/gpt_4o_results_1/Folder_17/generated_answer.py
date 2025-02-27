def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and ((i, j) not in checked_pairs) and ((j, i) not in checked_pairs):
                if sorted_lower(strings[i]) == sorted_lower(strings[j]):
                    anagram_pairs += 1
                checked_pairs.add((i, j))
    return anagram_pairs <= 22