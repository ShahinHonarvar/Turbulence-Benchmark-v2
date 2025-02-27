def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 90):
        substring = s[i:i + 91]
        if len(set(substring)) == 91:
            result.append(substring)
    return result