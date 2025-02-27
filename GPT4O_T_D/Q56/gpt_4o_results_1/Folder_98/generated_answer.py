def all_substring_of_size_n(s):
    unique_subs = set()
    for i in range(len(s) - 9):
        substr = s[i:i + 10]
        if len(substr) == 10 and len(set(substr)) == 10:
            unique_subs.add(substr)
    return list(unique_subs)