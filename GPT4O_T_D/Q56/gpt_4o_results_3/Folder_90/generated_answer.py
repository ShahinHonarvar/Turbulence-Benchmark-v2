def all_substring_of_size_n(s):
    result = []
    seen = set()
    for i in range(len(s) - 129):
        substr = s[i:i + 130]
        if substr not in seen and len(set(substr)) == 130:
            result.append(substr)
            seen.add(substr)
    return result