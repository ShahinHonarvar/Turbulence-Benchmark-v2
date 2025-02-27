def all_substring_of_size_n(s):
    return [s[i:i + 97] for i in range(len(s) - 96) if len(set(s[i:i + 97])) == 97]