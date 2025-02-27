def return_binary_or_hexa(input_tuple):
    a = input_tuple[7]
    b = input_tuple[9]
    present_numbers = set(input_tuple[7:10])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()