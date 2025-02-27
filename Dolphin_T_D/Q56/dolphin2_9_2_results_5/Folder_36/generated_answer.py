def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 145):
        sub = s[i:i + 146]
        if len(set(sub)) == 146:
            result.append(sub)
    return result