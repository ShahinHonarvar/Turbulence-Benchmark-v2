def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    target_length = 45
    for i in range(n - target_length + 1):
        substring = s[i:i + target_length]
        if len(set(substring)) == target_length:
            substrings.add(substring)
    return list(substrings)