def all_substring_of_size_n(s):
    if len(s) < 84:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if len(substring) == 84 and substring not in seen and (len(set(substring)) == 84):
            result.append(substring)
            seen.add(substring)
    return result