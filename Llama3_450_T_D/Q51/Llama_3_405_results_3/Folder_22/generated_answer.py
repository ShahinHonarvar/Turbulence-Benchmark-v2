def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = 0
    for v in anagrams.values():
        if len(v) > 1 and len(v[0]) >= 3:
            count += 1
        if count > 14:
            return False
    return True