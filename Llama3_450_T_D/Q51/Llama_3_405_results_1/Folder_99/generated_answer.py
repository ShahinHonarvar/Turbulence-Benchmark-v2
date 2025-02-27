def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            count += 1
            if count > 93:
                return False
        else:
            anagrams[sorted_str] = True
    return True