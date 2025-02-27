def find_subset_of_length_n(elements):
    n = 84
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                for l in range(k + 1, len(elements)):
                    for m in range(l + 1, len(elements)):
                        for o in range(m + 1, len(elements)):
                            for p in range(o + 1, len(elements)):
                                for q in range(p + 1, len(elements)):
                                    for r in range(q + 1, len(elements)):
                                        subset = {elements[i], elements[j], elements[k], elements[l], elements[m], elements[o], elements[p], elements[q], elements[r]}
                                        if len(subset) == n:
                                            count += 1
    return count