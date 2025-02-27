def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            count += len(anagrams[key])
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return count >= 314