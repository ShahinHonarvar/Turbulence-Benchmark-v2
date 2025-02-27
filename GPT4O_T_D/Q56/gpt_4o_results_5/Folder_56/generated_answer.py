def all_substring_of_size_n(s):
    if len(s) < 69:
        return []
    substrings = set()
    seen = set()
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if substring not in seen and len(set(substring)) == 69:
            substrings.add(substring)
            seen.add(substring)
    return list(substrings)