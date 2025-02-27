def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 73):
        if len(set(s[i:i + 74])) == 74:
            result.append(s[i:i + 74])
    return list(set(result))