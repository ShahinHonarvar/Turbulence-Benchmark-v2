def all_substring_of_size_n(s):
    if len(s) < 54:
        return []
    res = []
    seen_substrings = set()
    for i in range(len(s) - 53):
        substring = s[i:i + 54]
        if len(set(substring)) == 54:
            if substring not in seen_substrings:
                res.append(substring)
                seen_substrings.add(substring)
    return res