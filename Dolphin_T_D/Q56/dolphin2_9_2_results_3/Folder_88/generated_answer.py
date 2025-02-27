def all_substring_of_size_n(s):
    if len(s) < 68:
        return []
    result = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)