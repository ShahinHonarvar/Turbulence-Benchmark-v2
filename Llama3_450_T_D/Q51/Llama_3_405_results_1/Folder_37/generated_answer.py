def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    count = 0
    for a in anagrams.values():
        count += len(a) * (len(a) - 1) // 2
        if count > 206:
            return False
    return True