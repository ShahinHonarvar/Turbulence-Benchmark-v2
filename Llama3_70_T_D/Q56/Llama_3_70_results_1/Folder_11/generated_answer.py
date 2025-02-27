def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 78 + 1):
        substring = s[i:i + 78]
        if len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)