def all_substring_of_size_n(s):
    result = []
    seen = set()
    n = 77
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) == len(set(substr)) and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result