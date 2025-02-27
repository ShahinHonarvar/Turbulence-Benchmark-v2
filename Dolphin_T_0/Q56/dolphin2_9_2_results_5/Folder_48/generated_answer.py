def all_substring_of_size_n(string):
    n = 120
    string_length = len(string)
    if string_length < n:
        return []
    substrings = set()
    for i in range(string_length - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)