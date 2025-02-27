def if_contains_anagrams(strings):
    freq = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
    pairs = sum((val * (val - 1) // 2 for val in freq.values()))
    return pairs <= 74