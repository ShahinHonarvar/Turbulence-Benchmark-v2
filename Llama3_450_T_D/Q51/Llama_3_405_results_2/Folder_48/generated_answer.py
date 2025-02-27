def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            count += len(anagrams[sorted_str])
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    return count <= 277