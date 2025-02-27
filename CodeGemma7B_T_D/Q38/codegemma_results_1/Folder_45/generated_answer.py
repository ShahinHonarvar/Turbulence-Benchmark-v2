def find_subset_of_length_n(set_):
    num = 0
    for i in set_:
        for j in set_:
            for k in set_:
                if i != j or j != k or k != i:
                    num += 1
    return num