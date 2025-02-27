def all_substring_of_size_n(s):
    result = []
    n = len(s)
    seen = set()
    for i in range(n - 49):
        substr = s[i:i + 50]
        if len(set(substr)) == 50 and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result