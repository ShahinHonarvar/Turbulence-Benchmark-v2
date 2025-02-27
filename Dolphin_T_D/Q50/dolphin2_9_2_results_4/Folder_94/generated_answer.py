def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst_i = lst[i].lower()
                lst_j = lst[j].lower()
                if sorted(lst_i) == sorted(lst_j):
                    anagram_pairs += 1
    return anagram_pairs >= 46