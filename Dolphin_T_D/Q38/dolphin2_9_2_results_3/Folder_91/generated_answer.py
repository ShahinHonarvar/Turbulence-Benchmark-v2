def find_subset_of_length_n(s):
    if len(s) < 6:
        return 0
    else:
        comb = 1
        for i in range(6, len(s) + 1):
            comb *= i
        comb /= 720
        return int(comb)