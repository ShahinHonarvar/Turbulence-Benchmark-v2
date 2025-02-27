def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 32):
        sub = s[i:i + 33]
        if len(set(sub)) == 33 and sub not in result:
            result.append(sub)
    return result