def all_substring_of_size_n(s):
    if len(s) < 2:
        return []
    substrings = set()
    for i in range(len(s) - 1):
        temp = s[i:i + 2]
        if len(set(temp)) == len(temp):
            substrings.add(temp)
    return list(substrings)