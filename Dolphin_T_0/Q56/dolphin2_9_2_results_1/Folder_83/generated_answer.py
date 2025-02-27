def all_substring_of_size_n(s):
    if len(s) < 48:
        return []
    substrings = set()
    for i in range(len(s) - 47):
        if s[i:i + 48].isalpha() and len(set(s[i:i + 48])) == 48:
            substrings.add(s[i:i + 48])
    return list(substrings)