def find_subset_of_length_n(s):
    res = 0
    for i in range(len(s) + 1):
        if i == 72:
            res += 1
        elif i > 72:
            break
        else:
            for comb in itertools.combinations(s, i):
                res += 1
    return res