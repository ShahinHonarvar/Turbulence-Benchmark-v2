def if_contains_anagrams(strings):
    d = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
    count = 0
    for key in d:
        count += d[key] * (d[key] - 1) // 2
    return count >= 22