def all_substring_of_size_n(s):
    return list(set([s[i:i + 50] for i in range(len(s) - 49) if len(set(s[i:i + 50])) == 50]))