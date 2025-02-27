def all_substring_of_size_n(s):
    return [s[i:i + 87] for i in range(len(s) - 87 + 1) if len(set(s[i:i + 87])) == 87]