def all_substring_of_size_n(s):
    substrings = [s[i:i + 91] for i in range(len(s) - 90) if len(set(s[i:i + 91])) == 91]
    return list(set(substrings))