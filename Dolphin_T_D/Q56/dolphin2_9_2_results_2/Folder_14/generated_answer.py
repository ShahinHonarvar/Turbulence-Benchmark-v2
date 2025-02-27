def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 84):
        sub = s[i:i + 85]
        if len(set(sub)) == 85:
            result.append(sub)
    return set(result)