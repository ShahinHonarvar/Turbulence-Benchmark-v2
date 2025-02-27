def all_substring_of_size_n(s):
    return list({s[i:i + 35] for i in range(len(s) - 34)})