def find_subset_of_length_n(elements_set):
    if len(elements_set) < 7:
        return set()
    elif len(elements_set) == 7:
        return {frozenset(elements_set)}
    else:
        subset_count = 0
        for i in range(len(elements_set) - 6):
            for j in range(i + 1, len(elements_set) - 5):
                for k in range(j + 1, len(elements_set) - 4):
                    for l in range(k + 1, len(elements_set) - 3):
                        for m in range(l + 1, len(elements_set) - 2):
                            for n in range(m + 1, len(elements_set) - 1):
                                for o in range(n + 1, len(elements_set)):
                                    subset = frozenset((elements_set[i], elements_set[j], elements_set[k], elements_set[l], elements_set[m], elements_set[n], elements_set[o]))
                                    subset_count += 1
        return subset_count