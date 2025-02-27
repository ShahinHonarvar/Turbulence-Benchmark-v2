def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = ''.join(sorted(lst[i].lower()))
            s2 = ''.join(sorted(lst[j].lower()))
            if s1 == s2 and len(s1) >= 3 and (lst[i].lower() != lst[j].lower()):
                anagram_count += 1
    return anagram_count >= 93