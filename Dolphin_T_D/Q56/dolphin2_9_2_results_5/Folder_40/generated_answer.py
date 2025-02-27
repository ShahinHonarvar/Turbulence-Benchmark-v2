def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 1):
        sub = s[i:i + 2]
        if sub not in result and len(set(sub)) == 2:
            result.append(sub)
    return result