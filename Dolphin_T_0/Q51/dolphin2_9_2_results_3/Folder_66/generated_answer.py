def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                if anagrams[sorted_s] >= 2:
                    return True
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    return False