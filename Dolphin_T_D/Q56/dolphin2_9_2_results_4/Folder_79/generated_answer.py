def all_substring_of_size_n(s):
    if len(s) < 61:
        return []
    return [s[i:i + 61] for i in range(len(s) - 60) if len(set(s[i:i + 61])) == 61]