def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for s in strings:
        t = tuple(sorted((d.lower() for d in re.findall('\\b\\w{3,}\\b', s))))
        if t not in anagrams:
            anagrams[t] = 1
        else:
            anagrams[t] += 1
            pairs += 1
            if pairs > 50:
                return False
    return True