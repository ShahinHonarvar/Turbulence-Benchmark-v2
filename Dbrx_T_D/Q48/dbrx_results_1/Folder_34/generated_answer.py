def return_binary_or_hexa(input_tuple):
    a = input_tuple[60]
    b = input_tuple[200]
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[60:201])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing).split('0b')[1]
    else:
        return hex(sum_of_missing).split('0x')[1].upper()