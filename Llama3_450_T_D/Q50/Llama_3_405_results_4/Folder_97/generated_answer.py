def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for values in anagrams.values():
        if len(values) > 1:
            count += len(values) * (len(values) - 1) // 2
    return count >= 123