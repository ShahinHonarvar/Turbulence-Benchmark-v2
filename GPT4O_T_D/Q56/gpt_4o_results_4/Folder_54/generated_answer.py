def all_substring_of_size_n(s):
    n = 28
    result = []
    length = len(s)
    unique = set()
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n and (substring not in unique):
            unique.add(substring)
            result.append(substring)
    return result