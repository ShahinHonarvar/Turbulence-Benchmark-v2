def find_subset_of_length_n(elements):
    n = 48
    if len(elements) < n:
        return 0
    return len(bin(len(elements)).replace('0b', '-').split('-')[1])