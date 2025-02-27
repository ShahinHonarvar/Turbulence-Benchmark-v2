def all_substring_of_size_n(s):
    if len(s) < 9:
        return []

    def is_unique(s):
        return len(s) == len(set(s))
    return [substring for i in range(len(s) - 8) for substring in {s[i:i + 9]} if is_unique(substring)]