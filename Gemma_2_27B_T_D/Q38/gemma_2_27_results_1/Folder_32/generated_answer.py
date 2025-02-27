def find_subset_of_length_n(elements):
    n = 22
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            subset = set()
            for k in range(i, i + n):
                if k < len(elements):
                    subset.add(elements[k])
            if len(subset) == n:
                count += 1
    return count