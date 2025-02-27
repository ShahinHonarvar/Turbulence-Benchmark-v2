def all_substring_of_size_n(s):
    unique_substrings = []
    n = 57
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            unique_substrings.append(substring)
    return unique_substrings