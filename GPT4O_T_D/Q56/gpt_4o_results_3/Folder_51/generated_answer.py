def all_substring_of_size_n(s):
    if len(s) < 96:
        return []
    result = []
    seen = set()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if substring not in seen and len(set(substring)) == 96:
            result.append(substring)
            seen.add(substring)
    return result