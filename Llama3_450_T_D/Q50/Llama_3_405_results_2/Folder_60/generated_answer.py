def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s_lower)
        else:
            anagrams[sorted_str] = [s_lower]
    count = 0
    for key, value in anagrams.items():
        if len(value) > 1 and len(key) >= 3:
            n = len(value)
            count += n * (n - 1) // 2
    return count >= 60