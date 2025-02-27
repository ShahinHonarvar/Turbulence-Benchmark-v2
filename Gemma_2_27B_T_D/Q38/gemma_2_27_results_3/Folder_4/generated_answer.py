def find_subset_of_length_n(input_set):
    total_subsets = 0
    for i in range(len(input_set)):
        for j in range(i + 1, len(input_set)):
            for k in range(j + 1, len(input_set)):
                for l in range(k + 1, len(input_set)):
                    for m in range(l + 1, len(input_set)):
                        for n in range(m + 1, len(input_set)):
                            for o in range(n + 1, len(input_set)):
                                for p in range(o + 1, len(input_set)):
                                    for q in range(p + 1, len(input_set)):
                                        for r in range(q + 1, len(input_set)):
                                            for s in range(r + 1, len(input_set)):
                                                for t in range(s + 1, len(input_set)):
                                                    total_subsets += 1
    return total_subsets