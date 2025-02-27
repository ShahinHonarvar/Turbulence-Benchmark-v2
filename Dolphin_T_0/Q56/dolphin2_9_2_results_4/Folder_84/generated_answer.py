def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    result = []
    for i in range(len(s) - 113):
        substring = s[i:i + 114]
        if len(set(substring)) == len(substring):
            result.append(substring)
    return result