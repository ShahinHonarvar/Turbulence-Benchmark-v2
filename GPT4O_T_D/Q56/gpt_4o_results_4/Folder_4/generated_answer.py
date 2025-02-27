def all_substring_of_size_n(s):
    n = 41
    substrings = []
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))