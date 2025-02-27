def find_subset_of_length_n(elements):
    n = 23
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            if len({*elements[i:j + 1]}) == n:
                count += 1
    return count