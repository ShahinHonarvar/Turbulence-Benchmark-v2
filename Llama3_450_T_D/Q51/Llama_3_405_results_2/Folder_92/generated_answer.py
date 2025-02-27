def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        if ''.join(sorted(s)) in anagrams:
            anagrams[''.join(sorted(s))].append(s)
        else:
            anagrams[''.join(sorted(s))] = [s]
    for a in anagrams.values():
        count += len(a) * (len(a) - 1) // 2
        if count > 34:
            return False
    return True