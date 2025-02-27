def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 63):
        substring = s[i:i + 64]
        if len(set(substring)) == 64 and substring not in result:
            result.append(substring)
    return result