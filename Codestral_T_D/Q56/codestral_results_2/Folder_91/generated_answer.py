def all_substring_of_size_n(s):
    return [s[i:i + 6] for i in range(len(s) - 5) if len(set(s[i:i + 6])) == 6]