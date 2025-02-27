def if_contains_anagrams(strings):
    counts = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            counts[key] = counts.get(key, 0) + 1
    return sum((v * (v - 1) // 2 for v in counts.values())) >= 246