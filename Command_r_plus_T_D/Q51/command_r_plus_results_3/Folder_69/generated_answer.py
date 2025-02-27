def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                normalized_i = normalize(lst[i])
                normalized_j = normalize(lst[j])
                if normalized_i == normalized_j and (normalized_i, normalized_j) not in anagram_set:
                    anagram_count += 1
                    anagram_set.add((normalized_i, normalized_j))
                    if anagram_count > 58:
                        return False
    return True