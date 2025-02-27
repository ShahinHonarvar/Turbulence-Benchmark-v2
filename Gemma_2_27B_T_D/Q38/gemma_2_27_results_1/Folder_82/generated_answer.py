def find_subset_of_length_n(input_set):
    n = 83
    count = 0
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            for k in range(j + 1, len(input_set)):
                for l in range(k + 1, len(input_set)):
                    for m in range(l + 1, len(input_set)):
                        for o in range(m + 1, len(input_set)):
                            for p in range(o + 1, len(input_set)):
                                for q in range(p + 1, len(input_set)):
                                    for r in range(q + 1, len(input_set)):
                                        for s in range(r + 1, len(input_set)):
                                            subset = {input_set[i], input_set[j], input_set[k], input_set[l], input_set[m], input_set[o], input_set[p], input_set[q], input_set[r], input_set[s]}
                                            if len(subset) == n:
                                                count += 1
    return count