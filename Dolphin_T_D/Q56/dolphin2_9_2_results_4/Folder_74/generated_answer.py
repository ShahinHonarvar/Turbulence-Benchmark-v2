def all_substring_of_size_n(string):
    if len(string) < 97:
        return []
    subs = []
    for start in range(0, len(string) - 96):
        sub = string[start:start + 97]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return subs