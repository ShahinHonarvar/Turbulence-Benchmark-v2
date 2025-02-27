def return_binary_or_hexa(num_tuple):
    a = num_tuple[10]
    b = num_tuple[28]
    missing_numbers = [i for i in range(a + 1, b) if i not in num_tuple[10:29]]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]