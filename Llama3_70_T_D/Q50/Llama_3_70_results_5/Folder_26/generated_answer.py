def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                anagrams_count += 1
    return anagrams_count >= 49