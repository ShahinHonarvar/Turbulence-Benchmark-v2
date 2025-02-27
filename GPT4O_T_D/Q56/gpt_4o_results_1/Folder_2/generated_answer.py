def all_substring_of_size_n(s):
    if len(s) < 56:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if len(set(substring)) == 56 and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result