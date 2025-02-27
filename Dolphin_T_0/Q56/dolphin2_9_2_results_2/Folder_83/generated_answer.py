def all_substring_of_size_n(string):
    subs = set()
    n = len(string)
    for i in range(n):
        for j in range(i + 48, n + 1):
            if len(set(string[i:j])) == 48:
                subs.add(string[i:j])
    return list(subs)