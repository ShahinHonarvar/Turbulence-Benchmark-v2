def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    for values in anagrams.values():
        count += len(values) * (len(values) - 1) // 2
    return count >= 44