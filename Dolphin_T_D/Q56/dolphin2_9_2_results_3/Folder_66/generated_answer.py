def all_substring_of_size_n(s):
    if len(s) < 26:
        return []
    substring = []
    for i in range(len(s) - 25):
        temp = set(s[i:i + 26])
        if len(temp) == 26:
            substring.append(''.join(temp))
    return substring