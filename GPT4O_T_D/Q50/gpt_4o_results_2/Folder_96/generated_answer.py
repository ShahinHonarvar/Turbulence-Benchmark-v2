def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                count += anagrams[sorted_s]
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    return count >= 98