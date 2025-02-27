def find_subset_of_length_n(elements):
    subsets_of_size_n = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                for l in range(k + 1, len(elements)):
                    for m in range(l + 1, len(elements)):
                        for n in range(m + 1, len(elements)):
                            if len({elements[i], elements[j], elements[k], elements[l], elements[m], elements[n]}) == 630:
                                subsets_of_size_n += 1
    return subsets_of_size_n