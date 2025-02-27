def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 11):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            result.append(substring)
    return list(set(result))