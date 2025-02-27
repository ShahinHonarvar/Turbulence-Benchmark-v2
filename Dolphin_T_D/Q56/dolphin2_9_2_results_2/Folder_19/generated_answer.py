def all_substring_of_size_n(string):
    if len(string) < 18:
        return []
    subs = []
    for i in range(len(string) - 17):
        sub = string[i:i + 18]
        if all((sub.count(c) == 1 for c in sub)):
            subs.append(sub)
    return subs