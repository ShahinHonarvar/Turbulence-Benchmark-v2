def all_substring_of_size_n(s):
    if len(s) < 31:
        return []
    n_substrings = []
    for i in range(len(s) - 29):
        substring = s[i:i + 31]
        if len(set(substring)) == len(substring):
            n_substrings.append(substring)
    return n_substrings