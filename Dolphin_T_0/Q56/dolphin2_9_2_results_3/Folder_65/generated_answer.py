def all_substring_of_size_n(s):
    if len(s) < 81:
        return []
    substrings = set()
    for i in range(len(s) - 80):
        sub = s[i:i + 81]
        if len(set(sub)) == len(sub) == 81:
            substrings.add(sub)
    return list(substrings)