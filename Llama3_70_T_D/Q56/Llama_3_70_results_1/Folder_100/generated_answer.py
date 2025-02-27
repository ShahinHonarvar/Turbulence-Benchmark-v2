def all_substring_of_size_n(s):
    return [s[i:i + 92] for i in range(len(s) - 91) if len(set(s[i:i + 92])) == 92]