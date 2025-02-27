def all_substring_of_size_n(s):
    size = 143
    seen = set()
    result = []
    for i in range(len(s) - size + 1):
        substring = s[i:i + size]
        if len(set(substring)) == size and substring not in seen:
            result.append(substring)
            seen.add(substring)
    return result