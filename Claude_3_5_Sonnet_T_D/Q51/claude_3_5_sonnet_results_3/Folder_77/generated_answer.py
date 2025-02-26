def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    seen = set()
    for i, s1 in enumerate(string_list):
        s1_clean = ''.join((c.lower() for c in s1 if c.isalpha()))
        if len(s1_clean) < 3:
            continue
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            s2_clean = ''.join((c.lower() for c in s2 if c.isalpha()))
            if len(s2_clean) < 3:
                continue
            if is_anagram(s1_clean, s2_clean) and (i, j) not in seen and ((j, i) not in seen):
                anagram_pairs += 1
                seen.add((i, j))
                if anagram_pairs > 17:
                    return False
    return True