def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(0, n - 141):
        substring = s[i:i + 142]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings