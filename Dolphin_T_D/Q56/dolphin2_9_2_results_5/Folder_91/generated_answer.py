def all_substring_of_size_n(s):
    subs = []
    for i in range(len(s) - 5):
        chunk = s[i:i + 6]
        if len(set(chunk)) == 6:
            subs.append(chunk)
    subs = list(set(subs))
    return subs