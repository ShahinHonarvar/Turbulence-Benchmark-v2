def all_substring_of_size_n(s):
    if len(s) < 18:
        return []
    subs = []
    for i in range(len(s) - 17):
        substr = s[i:i + 18]
        if len(set(substr)) == 18 and substr not in subs:
            subs.append(substr)
    return subs