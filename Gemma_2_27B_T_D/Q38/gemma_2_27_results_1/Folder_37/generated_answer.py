def find_subset_of_length_n(elements):
    n = 28
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            subset = set([elements[i], elements[j]])
            for k in range(j + 1, len(elements)):
                subset.add(elements[k])
                if len(subset) == n:
                    count += 1
                elif len(subset) > n:
                    break
    return count