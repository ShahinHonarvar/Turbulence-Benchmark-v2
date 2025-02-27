def all_substring_of_size_n(s):
    for substring in [s[i:i + 46] for i in range(len(s) - 45)]:
        if len(set(substring)) == 46:
            return list(substring)
    return []