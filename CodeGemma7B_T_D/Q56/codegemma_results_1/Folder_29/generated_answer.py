def all_substring_of_size_n(s):
    if len(s) >= 95:
        return [s[i:i + 95] for i in range(len(s) - 94)]
    else:
        return []