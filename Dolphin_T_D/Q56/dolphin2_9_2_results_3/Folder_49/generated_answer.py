def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 72):
        x = s[i:i + 73]
        if len(set(x)) == 73:
            result.append(x)
    return result