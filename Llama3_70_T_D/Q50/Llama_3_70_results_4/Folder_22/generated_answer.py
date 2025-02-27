def if_contains_anagrams(lst):
    anagram_count = 0
    lst_lower = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    for i in range(len(lst_lower)):
        for j in range(i + 1, len(lst_lower)):
            if lst_lower[i] == lst_lower[j]:
                anagram_count += 1
                if anagram_count >= 72:
                    return True
    return False