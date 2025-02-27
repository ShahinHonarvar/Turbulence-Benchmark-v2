def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            for k in range(j + 1, len(elements)):
                if len({elements[i], elements[j], elements[k]}) == 300:
                    count += 1
    return count