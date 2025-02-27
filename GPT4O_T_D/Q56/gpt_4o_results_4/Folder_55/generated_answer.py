def all_substring_of_size_n(s):
    result = []
    seen = set()
    n = len(s)
    for i in range(n - 39):
        substring = s[i:i + 40]
        if len(substring) == 40 and substring not in seen and (len(set(substring)) == 40):
            result.append(substring)
            seen.add(substring)
    return result