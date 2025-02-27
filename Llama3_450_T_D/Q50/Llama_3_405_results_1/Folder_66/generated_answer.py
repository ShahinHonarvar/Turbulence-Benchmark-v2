def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            count += anagrams[sorted_s]
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    return count >= 92