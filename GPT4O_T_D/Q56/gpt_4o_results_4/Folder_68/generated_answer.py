def all_substring_of_size_n(s):
    if len(s) < 75:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 74):
        substr = s[i:i + 75]
        if len(set(substr)) == 75 and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result