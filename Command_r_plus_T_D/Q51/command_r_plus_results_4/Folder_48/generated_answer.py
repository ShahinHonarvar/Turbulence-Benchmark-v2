def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        normalized_str_i = normalize_string(lst[i])
        if len(normalized_str_i) < 3:
            continue
        for j in range(i + 1, len(lst)):
            normalized_str_j = normalize_string(lst[j])
            if len(normalized_str_j) < 3:
                continue
            if normalized_str_i == normalized_str_j:
                anagram_pair = tuple(sorted((lst[i], lst[j])))
                if anagram_pair not in anagram_pairs:
                    anagram_pairs.add(anagram_pair)
                    anagram_count += 1
            if anagram_count > 277:
                return False
    return True