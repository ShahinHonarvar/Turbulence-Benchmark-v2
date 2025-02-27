def all_substring_of_size_n(string):
    subs = []
    for i in range(len(string)):
        for j in range(i + 10, len(string) + 1):
            sub = string[i:j]
            if len(set(sub)) == 10:
                subs.append(sub)
    return list(set(subs))