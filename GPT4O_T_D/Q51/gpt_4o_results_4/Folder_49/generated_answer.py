def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            sorted_str_i = sorted_string(strings[i])
            sorted_str_j = sorted_string(strings[j])
            if sorted_str_i == sorted_str_j and (i, j) not in checked_pairs:
                anagram_pairs += 1
                checked_pairs.add((i, j))
                if anagram_pairs > 10:
                    return False
    return True