def all_substring_of_size_n(s):
    if len(set(s)) < 143:
        return []
    result = set()
    for i in range(len(s) - 142):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            result.add(substring)
    return list(result)