def all_substring_of_size_n(s):
    return set([s[i:i + 143] for i in range(len(s) - 143 + 1)])