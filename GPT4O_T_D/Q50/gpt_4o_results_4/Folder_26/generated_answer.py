def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count >= 49:
                return True
    return False