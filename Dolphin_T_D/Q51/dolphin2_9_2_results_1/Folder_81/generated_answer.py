def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                s1 = sorted(lst[i].lower())
                s2 = sorted(lst[j].lower())
                if s1 == s2:
                    anagram_count += 1
    return anagram_count <= 79