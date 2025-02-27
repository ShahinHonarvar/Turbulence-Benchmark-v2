def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 90 + 1):
        substring = s[i:i + 90]
        if len(set(substring)) == 90 and substring not in result:
            result.append(substring)
    return result