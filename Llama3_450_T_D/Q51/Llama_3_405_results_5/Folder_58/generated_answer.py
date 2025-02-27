def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    count = 0
    for key in anagrams:
        if len(key) >= 3 and anagrams[key] > 1:
            count += anagrams[key] * (anagrams[key] - 1) // 2
        if count > 60:
            return False
    return True