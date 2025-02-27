def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += 1
        if count >= 22:
            return True
    return False