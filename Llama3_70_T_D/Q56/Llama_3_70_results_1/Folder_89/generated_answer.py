def all_substring_of_size_n(s):
    return [s[i:i + 38] for i in range(len(s) - 37) if len(set(s[i:i + 38])) == 38]