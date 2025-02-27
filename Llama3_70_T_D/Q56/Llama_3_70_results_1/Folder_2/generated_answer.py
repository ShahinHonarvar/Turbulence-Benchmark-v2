def all_substring_of_size_n(s):
    return [s[i:i + 56] for i in range(len(s) - 55) if len(set(s[i:i + 56])) == 56]