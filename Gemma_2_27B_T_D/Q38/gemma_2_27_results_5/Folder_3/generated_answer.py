def find_subset_of_length_n(elements):
    n = 100
    subsets = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                if len(set([elements[i], elements[j], elements[k], ..., elements[l]])) == n:
                    subsets += 1
    return subsets