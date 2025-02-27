def all_substring_of_size_n(s):
    substrings = [s[i:i + 146] for i in range(len(s) - 145) if len(set(s[i:i + 146])) == 146]
    return list(set(substrings))