def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = lst[i].lower()
            s2 = lst[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                anagram_count += 1
                if anagram_count >= 35:
                    return True
    return False