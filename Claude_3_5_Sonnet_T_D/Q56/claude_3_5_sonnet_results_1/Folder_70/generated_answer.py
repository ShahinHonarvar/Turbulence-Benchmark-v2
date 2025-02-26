def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            result.add(substring)
    return list(result)