def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        if key in anagrams:
            count += 1
            if count > 93:
                return False
        else:
            anagrams[key] = 1
    return True