def all_substring_of_size_n(s):
    if len(s) < 75:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 74):
        substring = s[i:i + 75]
        if len(set(substring)) == 75 and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result