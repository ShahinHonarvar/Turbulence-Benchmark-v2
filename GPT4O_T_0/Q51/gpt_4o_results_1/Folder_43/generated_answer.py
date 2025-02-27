def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if (i, j) not in checked_pairs:
                if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                    if sorted_string(strings[i]) == sorted_string(strings[j]):
                        anagram_pairs += 1
                        if anagram_pairs > 3:
                            return False
                checked_pairs.add((i, j))
    return True