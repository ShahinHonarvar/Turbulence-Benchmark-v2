def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if len(set(substring)) == len(substring):
            result.append(substring)
    return result