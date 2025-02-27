def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length):
        for j in range(i + 3, length + 1):
            if len(set(s[i:j])) == 30:
                result.append(s[i:j])
    return result