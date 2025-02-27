def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join(sorted(text.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        normalized_i = normalize_text(lst[i])
        if len(normalized_i) < 3:
            continue
        for j in range(i + 1, len(lst)):
            normalized_j = normalize_text(lst[j])
            if normalized_i == normalized_j:
                anagram_pair = tuple(sorted((lst[i], lst[j])))
                if anagram_pair not in anagram_pairs:
                    anagram_pairs.add(anagram_pair)
                    anagram_count += 1
    return anagram_count <= 277