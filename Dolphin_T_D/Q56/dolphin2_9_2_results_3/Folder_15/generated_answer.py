def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) == 3:
            if s[i:i + 3] not in result:
                result.append(s[i:i + 3])
    return result