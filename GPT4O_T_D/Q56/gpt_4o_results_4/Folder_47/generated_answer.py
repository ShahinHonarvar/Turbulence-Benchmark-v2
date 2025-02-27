def all_substring_of_size_n(s):
    if len(s) < 91:
        return []
    n = len(s)
    result = []
    seen = set()
    for i in range(n - 90):
        substring = s[i:i + 91]
        if len(set(substring)) == 91 and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result