def if_contains_anagrams(strings):
    result = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key not in result:
                result[key] = 1
            else:
                result[key] += 1
    pairs = sum([v * (v - 1) // 2 for v in result.values() if v > 1])
    return pairs <= 48