def return_binary_or_hexa(num_tuple):
    a = num_tuple[46]
    b = num_tuple[91]
    missing_numbers = [i for i in range(a + 1, b) if i not in num_tuple[46:92]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]