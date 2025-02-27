def all_substring_of_size_n(s):
    return [s[i:i + 143] for i in range(len(s) - 143 + 1) if len(set(s[i:i + 143])) == 143]