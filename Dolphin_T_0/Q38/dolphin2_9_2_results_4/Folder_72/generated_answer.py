def find_subset_of_length_n(elements):
    length = 16
    result = 0
    for i in range(len(elements) + 1):
        if i == length:
            result += 1
        elif i > length:
            result += len(elements) - i + 1
    return result