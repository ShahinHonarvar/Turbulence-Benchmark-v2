def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            s1, s2 = (string_list[i].lower(), string_list[j].lower())
            if len(s1) < 3 or len(s2) < 3:
                continue
            if len(s1) != len(s2):
                continue
            if (s1, s2) in seen or (s2, s1) in seen:
                continue
            if sorted(s1) == sorted(s2):
                anagram_count += 1
                seen.add((s1, s2))
                if anagram_count >= 26:
                    return True
    return False