def find_subset_of_length_n(elements):
    n = 97
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                ...
                for m in range(n - 1 + i, len(elements)):
                    subset = set(elements[i:m + 1])
                    if len(subset) == n:
                        count += 1
    return count