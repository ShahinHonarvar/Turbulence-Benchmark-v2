def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                norm_i = normalize(lst[i])
                norm_j = normalize(lst[j])
                if norm_i == norm_j and (norm_i, norm_j) not in anagram_set and ((norm_j, norm_i) not in anagram_set):
                    anagram_count += 1
                    anagram_set.add((norm_i, norm_j))
                    if anagram_count > 68:
                        return False
    return True