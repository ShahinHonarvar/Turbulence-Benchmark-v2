def if_contains_anagrams(word_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                normalized_i = normalize_string(word_list[i])
                normalized_j = normalize_string(word_list[j])
                if normalized_i == normalized_j:
                    anagram_pair = tuple(sorted((word_list[i], word_list[j])))
                    if anagram_pair not in anagram_pairs:
                        anagram_pairs.add(anagram_pair)
                        anagram_count += 1
                    if anagram_count > 58:
                        return False
    return True