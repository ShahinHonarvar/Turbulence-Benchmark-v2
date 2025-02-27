def all_substring_of_size_n(s):
    substrings = [s[i:i + 25] for i in range(len(s) - 24)]
    return [sub for sub in set(substrings) if len(set(sub)) == 25]