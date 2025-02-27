def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 22):
        temp = s[i:i + 23]
        if len(set(temp)) == 23:
            result.append(temp)
    return result