def find_subset_of_length_n(elements):
    n = 630
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                for l in range(k + 1, len(elements)):
                    for m in range(l + 1, len(elements)):
                        for o in range(m + 1, len(elements)):
                            if len({elements[i], elements[j], elements[k], elements[l], elements[m], elements[o]}) == n:
                                count += 1
    return count