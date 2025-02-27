def all_substring_of_size_n(string):
    n = 58
    substrings = []
    for i in range(0, len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))