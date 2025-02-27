def find_subset_of_length_n(elements):
    subset_length = 327
    subsets = [set() for _ in range(len(elements))]
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            subsets[count] = elements[i] | elements[j]
            count += 1
    for k in range(3, subset_length + 1):
        for l in range(len(elements)):
            for m in range(l + 1, len(elements)):
                if len(subsets[l] | elements[m]) == k:
                    subsets[count] = subsets[l] | elements[m]
                    count += 1
    return sum((1 for s in subsets if len(s) == subset_length))