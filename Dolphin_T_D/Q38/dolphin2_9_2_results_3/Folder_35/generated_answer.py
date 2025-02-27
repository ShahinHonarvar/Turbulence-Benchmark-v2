def find_subset_of_length_n(s):
    if 300 > len(s):
        return 0
    else:
        combination = s.combination(300)
        return len(combination)