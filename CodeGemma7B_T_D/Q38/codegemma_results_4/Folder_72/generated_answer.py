def find_subset_of_length_n(set):
    count = 0
    for i in range(pow(2, len(set))):
        subset = list()
        for j in range(len(set)):
            if i & 2 ** j:
                subset.append(set[j])
        if len(subset) == 16:
            count += 1
    return count