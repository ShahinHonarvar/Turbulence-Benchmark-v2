def if_contains_anagrams(lst):
    lst = [''.join(sorted(set(x.lower()))) for x in lst if len(x) >= 3]
    anagrams_count = sum((1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[i] == lst[j]))
    return anagrams_count >= 70