def find_subset_of_length_n(elements):
    if len(elements) < 793:
        return 0
    else:
        count = 1
        for i in range(len(elements) - 793 + 1, len(elements) + 1):
            if i == len(elements):
                return count
            else:
                count = count + elements[i]
    return count