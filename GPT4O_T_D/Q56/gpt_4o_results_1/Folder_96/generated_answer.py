def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == 21:
            result.append(substring)
    return result