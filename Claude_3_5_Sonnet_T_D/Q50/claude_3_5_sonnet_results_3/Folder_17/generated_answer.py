def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if len(s1) < 3:
            continue
        s1_lower = s1.lower()
        s1_sorted = ''.join(sorted(s1_lower))
        if s1_sorted in processed:
            continue
        processed.add(s1_sorted)
        for s2 in string_list[i + 1:]:
            if len(s2) < 3:
                continue
            s2_lower = s2.lower()
            if s1_lower != s2_lower and sorted(s1_lower) == sorted(s2_lower):
                anagram_count += 1
                if anagram_count >= 97:
                    return True
    return False