def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 78):
        substring = s[i:i + 79]
        if len(set(substring)) == 79:
            result.append(substring)
    return result