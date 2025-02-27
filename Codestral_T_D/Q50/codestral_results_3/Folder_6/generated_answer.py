def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            if key in anagrams:
                anagrams[key].append(s)
                if len(anagrams[key]) >= 2:
                    return True
            else:
                anagrams[key] = [s]
    return False