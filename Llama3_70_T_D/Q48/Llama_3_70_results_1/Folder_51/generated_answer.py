def return_binary_or_hexa(num_tuple):
    a = num_tuple[6]
    b = num_tuple[9]
    specified_range = set(num_tuple[6:10])
    missing_numbers = [i for i in range(a + 1, b) if i not in specified_range]
    total = sum(missing_numbers)
    return bin(total)[2:] if total % 2 else hex(total)[2:]