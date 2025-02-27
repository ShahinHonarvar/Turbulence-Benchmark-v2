def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst]
    anagrams_count = sum((1 for i in range(len(lst) - 1) for j in range(i + 1, len(lst)) if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i]) == sorted(lst[j]))))
    return anagrams_count >= 38