def find_subset_of_length_n(elements):
    n = 45
    size = len(elements)
    result = 0
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                for l in range(k + 1, size):
                    if len({elements[i], elements[j], elements[k], elements[l]}) == n:
                        result += 1
    return result