def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    for k in anagrams:
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 96