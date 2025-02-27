def if_contains_anagrams(lst):
    pair_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            if len(s1) >= 3 and len(s2) >= 3 and (s1 == s2):
                pair_count += 1
    return pair_count >= 57