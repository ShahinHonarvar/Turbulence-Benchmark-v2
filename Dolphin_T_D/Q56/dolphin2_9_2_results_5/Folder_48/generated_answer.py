def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 119):
        temp = []
        for j in range(120):
            temp.append(s[i + j])
        if len(set(temp)) == 120:
            result.append(''.join(temp))
    return result