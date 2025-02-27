def all_substring_of_size_n(s):
    n = len(s)
    result = []
    seen = set()
    for i in range(n - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30 and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result