def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 116):
        sub = s[i:i + 117]
        if len(set(sub)) == len(sub) and sub not in result:
            result.append(sub)
    return result