def find_subset_of_length_n(elements):
    if len(elements) < 449:
        return 0
    count = 0
    for i in range(len(elements)):
        if i < 449:
            count += 1
        else:
            break
    return count