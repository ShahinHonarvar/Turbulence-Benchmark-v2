def all_substring_of_size_n(s):
    if len(set(s)) < 18:
        return []
    return [s[i:i + 18] for i in range(len(s) - 17) if len(set(s[i:i + 18])) == 18]