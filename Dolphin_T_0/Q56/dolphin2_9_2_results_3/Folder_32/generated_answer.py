def all_substring_of_size_n(s):
    if len(s) < 71:
        return []
    substrings = set()
    for i in range(len(s) - 70):
        temp = s[i:i + 71]
        if len(set(temp)) == len(temp):
            substrings.add(temp)
    return list(substrings)