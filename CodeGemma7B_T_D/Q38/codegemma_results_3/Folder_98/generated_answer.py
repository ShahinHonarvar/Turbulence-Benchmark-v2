def find_subset_of_length_n(set):
    count = 0
    for i in range(2 ** len(set)):
        binary = bin(i)[2:].zfill(len(set))
        subset = [element for i, element in enumerate(set) if binary[i] == '1']
        if len(subset) == 4:
            count += 1
    return count