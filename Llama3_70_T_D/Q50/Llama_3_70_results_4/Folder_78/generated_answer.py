def if_contains_anagrams(lst):
    anagrams_count = 0
    lst_lower = [s.lower() for s in lst]
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if len(lst_lower[i]) >= 3 and len(lst_lower[j]) >= 3:
                if sorted(lst_lower[i]) == sorted(lst_lower[j]):
                    anagrams_count += 1
    return anagrams_count >= 79