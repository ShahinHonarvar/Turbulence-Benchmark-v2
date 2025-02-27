def all_substring_of_size_n(s):
    return list(set([s[i:i + 9] for i in range(len(s) - 8) if len(set(s[i:i + 9])) == 9]))