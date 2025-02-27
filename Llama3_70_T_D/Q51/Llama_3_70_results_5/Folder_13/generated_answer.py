def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join((e for e in s if e.isalpha())).lower()
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count <= 54