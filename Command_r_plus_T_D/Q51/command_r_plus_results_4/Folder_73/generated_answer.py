def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                norm_i = normalize(lst[i])
                norm_j = normalize(lst[j])
                if norm_i == norm_j and (i, j) not in anagram_pairs and ((j, i) not in anagram_pairs):
                    anagram_count += 1
                    anagram_pairs.add((i, j))
                    if anagram_count > 279:
                        return False
    return True