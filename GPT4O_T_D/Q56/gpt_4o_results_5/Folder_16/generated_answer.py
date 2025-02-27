def all_substring_of_size_n(s):
    result = []
    n = 124
    length = len(s)
    if length < n:
        return result
    seen = set()
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result