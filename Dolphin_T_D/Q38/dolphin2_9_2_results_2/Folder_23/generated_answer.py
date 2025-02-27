def find_subset_of_length_n(input_set):
    res = 0
    for i in range(len(input_set) + 1):
        if i == 69:
            res += 1
        elif i > 69:
            break
        else:
            res += find_subset_of_length_n_rec(input_set, i)
    return res

def find_subset_of_length_n_rec(input_set, n):
    if n == 0:
        return 1
    else:
        res = 0
        for elem in input_set:
            new_set = input_set.copy()
            new_set.remove(elem)
            res += find_subset_of_length_n_rec(new_set, n - 1)
    return res