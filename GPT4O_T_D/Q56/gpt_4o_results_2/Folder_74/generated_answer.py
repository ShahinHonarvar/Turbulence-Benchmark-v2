def all_substring_of_size_n(s):
    result = []
    n = len(s)
    target_length = 97
    if n < target_length:
        return result
    seen = set()
    for i in range(n - target_length + 1):
        substring = s[i:i + target_length]
        if len(set(substring)) == target_length and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result