def all_substring_of_size_n(s):
    result = []
    n = len(s)
    target_length = 31
    for i in range(n - target_length + 1):
        substring = s[i:i + target_length]
        if len(substring) == target_length and len(set(substring)) == target_length:
            result.append(substring)
    return result