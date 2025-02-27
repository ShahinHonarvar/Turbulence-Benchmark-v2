def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 88):
        substring = s[i:i + 89]
        if len(set(substring)) == 89:
            result.append(substring)
    return result