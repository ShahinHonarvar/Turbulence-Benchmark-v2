def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 25):
        sub = s[i:i + 26]
        if len(set(sub)) == 26:
            if sub not in result:
                result.append(sub)
    return result