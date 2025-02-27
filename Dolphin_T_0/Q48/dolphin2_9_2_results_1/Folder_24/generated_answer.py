def return_binary_or_hexa(num_tuple):
    a = num_tuple[13]
    b = num_tuple[91]
    missing_numbers = [num for num in range(a + 1, b) if num not in num_tuple[13:92]]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]