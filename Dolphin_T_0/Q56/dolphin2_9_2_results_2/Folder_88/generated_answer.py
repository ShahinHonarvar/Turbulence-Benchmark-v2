def all_substring_of_size_n(string):
    subs = set()
    if len(string) < 68:
        return []
    for i in range(len(string) - 67):
        sub_string = string[i:i + 68]
        if len(set(sub_string)) == 68:
            subs.add(sub_string)
    return list(subs)