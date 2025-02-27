def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
        if count >= 52:
            return True
    return False