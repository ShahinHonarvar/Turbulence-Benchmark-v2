def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    for k in anagrams:
        if len(anagrams[k]) > 1:
            count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 26