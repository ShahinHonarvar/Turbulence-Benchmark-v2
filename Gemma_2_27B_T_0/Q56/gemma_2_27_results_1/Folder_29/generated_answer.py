def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if len(set(substring)) == 95:
            result.append(substring)
    return result