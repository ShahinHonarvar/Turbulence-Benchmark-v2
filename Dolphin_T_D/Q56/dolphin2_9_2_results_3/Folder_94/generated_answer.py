def all_substring_of_size_n(s):
    return [s[i:i + 70] for i in range(len(s) - 69) if len(set(s[i:i + 70])) == 70]