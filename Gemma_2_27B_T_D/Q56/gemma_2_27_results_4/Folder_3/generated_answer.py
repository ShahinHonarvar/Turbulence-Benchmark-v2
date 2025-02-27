def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 92):
        substring = s[i:i + 93]
        if len(set(substring)) == 93:
            result.append(substring)
    return result