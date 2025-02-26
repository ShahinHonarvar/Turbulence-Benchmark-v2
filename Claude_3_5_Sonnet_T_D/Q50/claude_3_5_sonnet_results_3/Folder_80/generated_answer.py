def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = set()
    for i, s1 in enumerate(string_list):
        s1 = s1.lower()
        if len(s1) < 3:
            continue
        sorted_s1 = ''.join(sorted(s1))
        if sorted_s1 in seen:
            continue
        seen.add(sorted_s1)
        for s2 in string_list[i + 1:]:
            s2 = s2.lower()
            if len(s2) < 3:
                continue
            if sorted_s1 == ''.join(sorted(s2)):
                anagram_count += 1
                if anagram_count >= 19:
                    return True
    return False