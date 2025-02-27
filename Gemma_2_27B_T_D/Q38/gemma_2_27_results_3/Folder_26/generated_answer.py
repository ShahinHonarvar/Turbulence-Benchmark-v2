def find_subset_of_length_n(elements):
    n = 25
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            subset = set([elements[i], elements[j]])
            if len(subset) == n:
                count += 1
    return count