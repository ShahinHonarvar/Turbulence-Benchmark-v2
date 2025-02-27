def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count > 74:
            return False
    return True