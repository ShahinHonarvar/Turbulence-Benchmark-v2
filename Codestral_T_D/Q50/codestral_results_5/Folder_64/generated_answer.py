def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 5