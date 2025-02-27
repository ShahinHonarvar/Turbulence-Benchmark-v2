def all_substring_of_size_n(s):
    length = len(s)
    result = []
    for i in range(length - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == len(substring):
            result.append(substring)
    return result