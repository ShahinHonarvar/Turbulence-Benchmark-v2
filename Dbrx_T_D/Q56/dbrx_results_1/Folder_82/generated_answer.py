def all_substring_of_size_n(s):
    results = []
    n = 100
    if n > len(s):
        return results
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(seen & set(substring)) == 0:
            results.append(substring)
            seen.update(substring)
    return results