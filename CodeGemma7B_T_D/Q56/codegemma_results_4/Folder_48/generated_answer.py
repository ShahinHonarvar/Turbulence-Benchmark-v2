def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 96 + 1):
        substring = s[i:i + 120]
        if len(substring) > 0 and substring not in result:
            result.append(substring)
    return result