def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s_lower = s.lower()
        sorted_chars = ''.join(sorted(s_lower))
        if sorted_chars in anagrams:
            anagrams[sorted_chars].append(s_lower)
        else:
            anagrams[sorted_chars] = [s_lower]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 94