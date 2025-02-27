def all_substring_of_size_n(s):
    return [s[i:i + 87] for i in range(len(s) - 86) if len(set(s[i:i + 87])) == 87]