def all_substring_of_size_n(s):
    return list(set([s[i:i + 149] for i in range(len(s) - 148) if len(set(s[i:i + 149])) == 149]))