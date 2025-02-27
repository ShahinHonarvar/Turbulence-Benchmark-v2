def if_contains_anagrams(s_list):
    s_list = [s.lower() for s in s_list]
    anagram_pairs = 0
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            s1 = s_list[i]
            s2 = s_list[j]
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                anagram_pairs += 1
                if anagram_pairs >= 11:
                    return True
    return False