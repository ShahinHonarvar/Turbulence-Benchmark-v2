def all_substring_of_size_n(s):
    if len(s) < 96:
        return []
    substrings = set()
    for i in range(len(s) - 95):
        sub = s[i:i + 96]
        if len(sub) == len(set(sub)):
            substrings.add(sub)
    return list(substrings)