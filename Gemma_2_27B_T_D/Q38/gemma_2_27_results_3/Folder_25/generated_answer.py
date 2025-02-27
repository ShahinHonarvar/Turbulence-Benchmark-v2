def find_subset_of_length_n(input_set):
    n = 90
    count = 0
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            for k in range(j + 1, len(input_set)):
                if len(set([input_set[i], input_set[j], input_set[k], ...])) == n:
                    count += 1
    return count