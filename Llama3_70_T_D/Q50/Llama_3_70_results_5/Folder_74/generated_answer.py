def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        sorted_s = ''.join(sorted(lower_s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
            if count >= 17:
                return True
    return count >= 17