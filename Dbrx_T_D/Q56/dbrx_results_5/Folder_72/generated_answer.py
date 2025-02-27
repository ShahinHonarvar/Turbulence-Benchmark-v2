def all_substring_of_size_n(s):
    if len(s) < 88:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 88 + 1):
        substring = s[i:i + 88]
        if len(set(substring)) == 88 and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result