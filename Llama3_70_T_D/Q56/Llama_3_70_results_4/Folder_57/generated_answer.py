def all_substring_of_size_n(s):
    return [s[i:i + 60] for i in range(len(s) - 59) if len(set(s[i:i + 60])) == 60]