def if_contains_anagrams(words_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                normalized_i = normalize_string(words_list[i])
                normalized_j = normalize_string(words_list[j])
                if normalized_i == normalized_j:
                    anagram_pairs.add(tuple(sorted([i, j])))
                    if len(anagram_pairs) > 22:
                        return False
    return True