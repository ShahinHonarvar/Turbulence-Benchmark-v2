def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            result.append(substring)
    return result