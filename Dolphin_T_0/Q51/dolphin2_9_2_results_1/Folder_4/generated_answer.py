def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            s = s.replace(' ', '').lower()
            s = ''.join(sorted(s))
            if s in anagrams:
                count += 1
            else:
                anagrams[s] = True
    return count <= 84