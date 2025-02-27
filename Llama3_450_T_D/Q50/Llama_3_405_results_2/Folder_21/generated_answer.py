def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for k in anagrams:
        if len(anagrams[k]) > 1:
            count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 136