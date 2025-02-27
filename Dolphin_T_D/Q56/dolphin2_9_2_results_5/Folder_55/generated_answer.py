def all_substring_of_size_n(s):
    if len(s) < 40:
        return []
    output = []
    for i in range(len(s) - 39):
        if len(set(s[i:i + 40])) == 40:
            output.append(s[i:i + 40])
    return output