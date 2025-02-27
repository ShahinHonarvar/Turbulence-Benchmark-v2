def all_substring_of_size_n(s):
    length = 41
    if len(s) < length:
        return []
    substrs = set()
    for i in range(len(s) - length + 1):
        temp = s[i:i + length]
        if len(set(temp)) == length:
            substrs.add(temp)
    return list(substrs)