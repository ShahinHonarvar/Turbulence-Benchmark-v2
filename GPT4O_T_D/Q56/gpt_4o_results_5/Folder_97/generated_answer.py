def all_substring_of_size_n(string):
    n = 142
    if len(string) < n:
        return []
    result = []
    seen = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i + n]
        if len(set(substr)) == n and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result