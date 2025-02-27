def all_substring_of_size_n(s):
    result = []
    seen = set()
    for i in range(len(s) - 44):
        substr = s[i:i + 45]
        if len(set(substr)) == 45 and substr not in seen:
            result.append(substr)
            seen.add(substr)
    return result