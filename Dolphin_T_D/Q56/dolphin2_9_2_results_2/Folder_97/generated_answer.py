def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    length = 142
    if len(s) < length:
        return []
    return [s[i:i + length] for i in range(len(s) - length + 1) if len(set(s[i:i + length])) == length]