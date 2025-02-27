def all_substring_of_size_n(s):
    n = 85
    result = []
    seen = set()
    length = len(s)
    if length < n:
        return result
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n and (substring not in seen):
            result.append(substring)
            seen.add(substring)
    return result