def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 73):
        sub = s[i:i + 74]
        if len(set(sub)) == len(sub) and len(sub) == 74:
            result.append(sub)
    return result