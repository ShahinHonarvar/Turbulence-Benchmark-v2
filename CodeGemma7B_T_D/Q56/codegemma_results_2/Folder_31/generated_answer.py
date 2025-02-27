def all_substring_of_size_n(string):
    if len(string) < 46:
        return []
    all_str = [string[i:i + 46] for i in range(len(string) - 45)]
    return list(set(all_str))