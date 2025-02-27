def all_substring_of_size_n(s):
    result = []
    n = 57
    length = len(s)
    if length < n:
        return result
    seen = set()
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)) and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result