def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_i = normalize_string(lst[i])
        if len(normalized_i) < 3:
            continue
        for j in range(i + 1, len(lst)):
            normalized_j = normalize_string(lst[j])
            if normalized_i == normalized_j:
                anagram_pair = tuple(sorted((lst[i], lst[j])))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 44:
                        return False
    return True