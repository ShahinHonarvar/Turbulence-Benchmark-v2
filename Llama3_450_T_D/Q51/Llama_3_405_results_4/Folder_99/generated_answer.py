def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        if key in anagrams:
            count += len(anagrams[key])
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return count <= 93