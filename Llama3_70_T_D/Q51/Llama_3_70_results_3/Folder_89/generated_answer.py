def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if lst.count(s) > 1:
            anagrams_count += lst.count(s) * (lst.count(s) - 1) // 2
        for t in lst[lst.index(s) + 1:]:
            if sorted_s == ''.join(sorted(t)):
                anagrams_count += 1
    return anagrams_count <= 73