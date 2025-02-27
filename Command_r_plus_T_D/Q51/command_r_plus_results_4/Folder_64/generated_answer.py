def if_contains_anagrams(words_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                normalized_i = normalize_string(words_list[i])
                normalized_j = normalize_string(words_list[j])
                if normalized_i == normalized_j:
                    anagram_pair = tuple(sorted([words_list[i], words_list[j]]))
                    if anagram_pair not in anagram_pairs:
                        anagram_pairs.add(anagram_pair)
                        anagram_count += 1
                    if anagram_count > 59:
                        return False
    return True