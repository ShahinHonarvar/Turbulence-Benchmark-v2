def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3 and substring not in result:
            result.append(substring)
    return result