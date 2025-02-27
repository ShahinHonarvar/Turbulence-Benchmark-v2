def all_substring_of_size_n(s):
    if len(s) < 24:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(set(substring)) == 24:
            if substring not in seen:
                seen.add(substring)
                result.append(substring)
    return result