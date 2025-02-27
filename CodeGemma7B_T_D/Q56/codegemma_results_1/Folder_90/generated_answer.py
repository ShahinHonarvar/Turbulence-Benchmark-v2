def all_substring_of_size_n(txt):
    subs = []
    for i in range(len(txt) - 130 + 1):
        j = i + 130
        subs.append(txt[i:j])
    return subs