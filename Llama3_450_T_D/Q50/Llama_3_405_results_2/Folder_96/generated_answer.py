def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams and len(s) >= 3:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 98