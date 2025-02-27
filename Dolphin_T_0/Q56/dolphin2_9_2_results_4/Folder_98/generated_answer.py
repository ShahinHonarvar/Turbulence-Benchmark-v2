def all_substring_of_size_n(txt):
    if len(txt) < 10:
        return []
    subsets = []
    for i in range(0, len(txt) - 9):
        if len(set(txt[i:i + 10])) == 10 and txt[i:i + 10] not in subsets:
            subsets.append(txt[i:i + 10])
    return subsets