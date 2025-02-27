def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 97