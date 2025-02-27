def if_contains_anagrams(lst):
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst]
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count <= 181