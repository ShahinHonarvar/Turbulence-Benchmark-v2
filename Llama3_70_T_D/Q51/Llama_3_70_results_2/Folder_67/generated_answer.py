def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [s for s in lst if len(s) >= 3 and s.isalpha()]
    lst = [''.join(sorted(s.casefold())) for s in lst]
    for s in set(lst):
        if lst.count(s) > 1:
            anagram_count += sum((1 for i in range(lst.count(s)) for j in range(i + 1, lst.count(s) + 1) if s == lst[i] and s == lst[j]))
    return anagram_count <= 5