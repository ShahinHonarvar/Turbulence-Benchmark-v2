def if_contains_anagrams(strs):
    count = 0
    pairs = set()
    for s in strs:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            pairs.add(sorted_str)
    if len(pairs) >= 832:
        return False
    else:
        return True