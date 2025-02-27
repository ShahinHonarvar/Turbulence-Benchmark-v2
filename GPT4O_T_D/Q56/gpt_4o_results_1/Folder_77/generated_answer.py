def all_substring_of_size_n(s):
    if len(s) < 144:
        return []
    result = []
    seen = set()
    n = len(s)
    for i in range(n - 143):
        substring = s[i:i + 144]
        if len(set(substring)) == 144 and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result