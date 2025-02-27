def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 46):
        substring = s[i:i + 47]
        if len(set(substring)) == 47:
            result.append(substring)
    return result