def is_distinct(s):
    return len(s) == len(set(s))

def all_substring_of_size_n(s, n=84):
    if n > len(s):
        return []
    return [substring for i in range(len(s) - n + 1) for substring in [s[i:i + n]] if is_distinct(substring)]