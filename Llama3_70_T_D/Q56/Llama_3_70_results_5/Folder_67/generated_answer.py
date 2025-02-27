def all_substring_of_size_n(s):
    substrings = [s[i:i + 43] for i in range(len(s) - 42) if len(set(s[i:i + 43])) == 43]
    return list(set(substrings))