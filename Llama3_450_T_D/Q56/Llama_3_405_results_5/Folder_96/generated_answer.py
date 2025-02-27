def all_substring_of_size_n(s):
    return list(set([s[i:i + 21] for i in range(len(s) - 20) if len(set(s[i:i + 21])) == 21]))