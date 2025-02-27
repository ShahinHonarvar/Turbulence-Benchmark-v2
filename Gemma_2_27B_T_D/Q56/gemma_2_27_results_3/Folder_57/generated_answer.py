def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if len(set(substring)) == 60 and substring not in result:
            result.append(substring)
    return result