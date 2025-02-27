def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
        if count >= 81:
            return True
    return False