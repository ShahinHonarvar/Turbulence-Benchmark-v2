def all_substring_of_size_n(s):
    n = 85
    seen = set()
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result