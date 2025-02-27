def all_substring_of_size_n(str_arg):
    if len(str_arg) < 29:
        return []
    all_seen_substrings = set()
    for idx in range(len(str_arg) - 28):
        sub_str = str_arg[idx:idx + 29]
        all_seen_substrings.add(sub_str)
    return list(all_seen_substrings)