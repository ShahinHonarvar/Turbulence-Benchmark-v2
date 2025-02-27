def all_substring_of_size_n(s):
    return [s[i:i + 89] for i in range(len(s) - 88) if len(set(s[i:i + 89])) == 89]