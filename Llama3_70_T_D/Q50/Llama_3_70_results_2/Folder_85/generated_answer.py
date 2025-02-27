def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].add(s)
        else:
            anagrams[sorted_s] = {s}
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 73