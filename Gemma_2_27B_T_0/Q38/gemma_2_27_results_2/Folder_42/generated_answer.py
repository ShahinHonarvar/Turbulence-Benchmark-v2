def find_subset_of_length_n(elements):
    n = 31
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                if len({elements[i], elements[j], elements[k]}) == n:
                    count += 1
    return count