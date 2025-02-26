def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 57):
        substring = s[i:i + 58]
        if len(set(substring)) == 58:
            if substring not in result:
                result.append(substring)
    return result