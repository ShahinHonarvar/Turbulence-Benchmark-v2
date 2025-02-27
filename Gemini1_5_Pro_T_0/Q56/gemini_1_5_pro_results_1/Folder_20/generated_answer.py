def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if len(set(substring)) == 50 and substring not in result:
            result.append(substring)
    return result