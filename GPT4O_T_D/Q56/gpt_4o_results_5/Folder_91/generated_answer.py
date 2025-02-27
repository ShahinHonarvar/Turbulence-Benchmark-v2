def all_substring_of_size_n(s):
    result = []
    seen = set()
    n = len(s)
    for i in range(n - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6 and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result