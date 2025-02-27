def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                anagrams_count += 1
                if anagrams_count >= 54:
                    return True
    return False