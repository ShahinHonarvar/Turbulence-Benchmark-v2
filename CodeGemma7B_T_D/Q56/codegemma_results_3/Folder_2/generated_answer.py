def all_substring_of_size_n(x):
    if len(x) < 56:
        return []
    all = []
    for i in range(len(x) - 55):
        all.append(x[i:i + 56])
    return list(set(all))