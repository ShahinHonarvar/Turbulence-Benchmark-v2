def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 13):
        substring = s[i:i + 14]
        if len(set(substring)) == 14:
            if substring not in result:
                result.append(substring)
    return result