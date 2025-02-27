def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for k in anagrams:
        n = len(anagrams[k])
        count += n * (n - 1) // 2
    return count >= 136