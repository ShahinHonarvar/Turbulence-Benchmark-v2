def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            for k in range(j, len(elements)):
                if len(elements[i] + elements[j] + elements[k]) == 95:
                    subset_count += 1
    return subset_count