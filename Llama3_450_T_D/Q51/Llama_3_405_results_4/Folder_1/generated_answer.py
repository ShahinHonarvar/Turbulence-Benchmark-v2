def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        if not s.isalpha():
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
        if count > 30:
            return False
    return True