def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for k in anagrams:
        if len(anagrams[k]) > 1:
            count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 94