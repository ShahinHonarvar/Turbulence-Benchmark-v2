def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    seen_pairs = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if is_anagram(string_list[i], string_list[j]):
                    pair = tuple(sorted([string_list[i], string_list[j]]))
                    if pair not in seen_pairs:
                        anagram_count += 1
                        seen_pairs.add(pair)
    return anagram_count <= 318