def all_substring_of_size_n(a):
    n = len(a)
    all_list = set()
    for i in range(n - 64 + 1):
        for j in range(i + 64):
            substring = a[i:j]
            if len(substring) == len(set(substring)):
                all_list.add(substring)
    return list(all_list)