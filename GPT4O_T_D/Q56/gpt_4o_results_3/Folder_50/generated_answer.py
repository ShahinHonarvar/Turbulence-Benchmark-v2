def all_substring_of_size_n(s):
    n = 11
    results = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            if substring not in results:
                results.append(substring)
    return results