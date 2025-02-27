def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if substring not in result:
            result.append(substring)
    return result