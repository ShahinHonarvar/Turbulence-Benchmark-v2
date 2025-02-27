def find_subset_of_length_n(input_set):
    n = 64
    count = 0
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            for k in range(j + 1, len(input_set)):
                for l in range(k + 1, len(input_set)):
                    for m in range(l + 1, len(input_set)):
                        for o in range(m + 1, len(input_set)):
                            if len({input_set[i], input_set[j], input_set[k], input_set[l], input_set[m], input_set[o]}) == n:
                                count += 1
    return count