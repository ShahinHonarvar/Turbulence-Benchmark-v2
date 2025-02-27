def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3 or not s_lower.isalpha():
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = sum((len(a) * (len(a) - 1) // 2 for a in anagrams.values() if len(a) > 1))
    return count <= 55