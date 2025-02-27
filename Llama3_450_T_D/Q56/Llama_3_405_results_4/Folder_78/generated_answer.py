def all_substring_of_size_n(s):
    return list(set([s[i:i + 49] for i in range(len(s) - 48) if len(set(s[i:i + 49])) == 49]))