def if_contains_anagrams(strs):
    anagrams = {}
    count = 0
    for s in strs:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for v in anagrams.values():
        if len(v) > 1:
            count += 1
    return count >= 5