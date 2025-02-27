def all_substring_of_size_n(string):
    length = len(string)
    subs = set()
    for i in range(length):
        for j in range(i + 9, min(i + 10, length + 1)):
            sub = string[i:j]
            if len(set(sub)) == len(sub):
                subs.add(sub)
    return list(subs)