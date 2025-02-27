def all_substring_of_size_n(s):
    if len(s) < 67:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 66):
        substring = s[i:i + 67]
        if len(set(substring)) == 67 and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result