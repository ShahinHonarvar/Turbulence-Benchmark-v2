def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52:
            result.append(substring)
    return list(set(result))