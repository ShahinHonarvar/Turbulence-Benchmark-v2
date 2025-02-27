def if_contains_anagrams(strs):
    anagrams = {}
    count = 0
    for s in strs:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count >= 46:
            return True
    return False