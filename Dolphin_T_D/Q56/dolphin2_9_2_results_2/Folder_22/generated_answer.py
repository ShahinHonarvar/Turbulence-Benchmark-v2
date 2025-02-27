def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        if len(set(s[i:i + 22])) == 22:
            result.append(s[i:i + 22])
    return list(set(result))