def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (lst[i].casefold() != lst[j].casefold()):
                s1 = ''.join(sorted(lst[i].casefold()))
                s2 = ''.join(sorted(lst[j].casefold()))
                if (s1, s2) not in seen and (s2, s1) not in seen and (s1 == s2):
                    count += 1
                    seen.add((s1, s2))
    return count >= 89