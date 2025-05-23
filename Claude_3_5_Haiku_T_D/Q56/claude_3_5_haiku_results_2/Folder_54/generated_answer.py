def all_substring_of_size_n(s):
    if len(s) < 28:
        return []
    result = []
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if len(set(substring)) == 28:
            if substring not in result:
                result.append(substring)
    return result