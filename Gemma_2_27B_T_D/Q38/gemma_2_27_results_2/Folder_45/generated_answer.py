def find_subset_of_length_n(elements):
    n = 33
    total_subsets = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                subset = {elements[i], elements[j], elements[k]}
                if len(subset) == n:
                    total_subsets += 1
    return total_subsets