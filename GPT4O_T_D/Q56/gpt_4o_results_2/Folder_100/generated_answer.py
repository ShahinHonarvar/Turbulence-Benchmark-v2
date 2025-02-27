def all_substring_of_size_n(s):
    if len(s) < 92:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 91):
        substr = s[i:i + 92]
        if len(set(substr)) == 92:
            if substr not in seen:
                seen.add(substr)
                result.append(substr)
    return result