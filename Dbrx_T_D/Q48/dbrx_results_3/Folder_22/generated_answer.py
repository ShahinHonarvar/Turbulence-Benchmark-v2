def return_binary_or_hexa(input_tuple):
    a = input_tuple[40]
    b = input_tuple[200]
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[41:200])
    if not missing_numbers:
        return ''
    else:
        sum_missing_numbers = sum(missing_numbers)
        if sum_missing_numbers % 2:
            return bin(sum_missing_numbers)[2:]
        else:
            return hex(sum_missing_numbers).split('x')[-1].upper()