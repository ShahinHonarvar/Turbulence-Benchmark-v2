def all_substring_of_size_n(s):
    if len(s) < 86:
        return []
    unique_substrs = set()
    for i in range(len(s) - 85):
        substring = s[i:i + 86]
        if len(set(substring)) == 86:
            unique_substrs.add(substring)
    return list(unique_substrs)