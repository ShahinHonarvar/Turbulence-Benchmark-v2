def find_subset_of_length_n(elements):
    n = 90
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                ...
                for z in range(n - 1 + i, len(elements)):
                    count += 1
    return count