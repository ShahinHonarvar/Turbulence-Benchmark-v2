def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16 + 1):
        if len(set(s[i:i + 16])) == 16 and s[i:i + 16] not in result:
            result.append(s[i:i + 16])
    return result