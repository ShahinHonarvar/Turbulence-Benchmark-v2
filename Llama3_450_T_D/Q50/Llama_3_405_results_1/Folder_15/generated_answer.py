def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = sum((len(val) > 1 for val in anagrams.values()))
    return count >= 4