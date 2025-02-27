def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_i = normalize(lst[i])
        if len(lst[i]) >= 3 and normalized_i not in anagram_set:
            anagram_set.add(normalized_i)
            for j in range(i + 1, len(lst)):
                normalized_j = normalize(lst[j])
                if normalized_i == normalized_j:
                    anagram_count += 1
                    anagram_set.add(normalized_j)
    return anagram_count <= 77