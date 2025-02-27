def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 72):
        subset = s[i:i + 73]
        if len(set(subset)) == 73:
            result.append(subset)
    return result