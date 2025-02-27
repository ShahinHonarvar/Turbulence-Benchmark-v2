def all_substring_of_size_n(s):
    return [s[i:i + 9] for i in range(len(s)) if len(set(s[i:i + 9])) == 9]