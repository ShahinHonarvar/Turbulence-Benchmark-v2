def find_subset_of_length_n(input_set):
    if len(input_set) < 894:
        return 0
    else:
        subset_count = 0
        for i in range(len(input_set) - 893):
            for j in range(i + 1, len(input_set) - 892):
                for k in range(j + 1, len(input_set) - 891):
                    current_subset = {input_set[i], input_set[j], input_set[k], ..., input_set[len(input_set) - 891]}
                    if len(current_subset) == 894:
                        subset_count += 1
        return subset_count