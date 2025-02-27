def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(words_list):
    anagram_pairs_count = 0
    anagram_set = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                normalized_i = normalize_string(words_list[i])
                normalized_j = normalize_string(words_list[j])
                if normalized_i == normalized_j and (normalized_i, normalized_j) not in anagram_set:
                    anagram_pairs_count += 1
                    anagram_set.add((normalized_i, normalized_j))
                    if anagram_pairs_count > 59:
                        return False
    return True