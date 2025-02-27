def all_substring_of_size_n(s):
    result = []
    for i in range(0, len(s) - 117 + 1):
        substring = s[i:i + 117]
        if len(set(substring)) == 117 and substring not in result:
            result.append(substring)
    return result