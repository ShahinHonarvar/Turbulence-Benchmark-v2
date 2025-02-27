def all_substring_of_size_n(s):
    if len(s) < 143:
        return []
    output = []
    for i in range(len(s) - 142):
        str = s[i:i + 143]
        if len(set(str)) == 143:
            output.append(str)
    return output