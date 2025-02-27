def return_binary_or_hexa(tuple):
    a = tuple[200]
    b = tuple[202]
    present_numbers = tuple[200:203]
    missing_numbers = [n for n in range(a + 1, b) if n not in present_numbers]
    if not missing_numbers:
        return ''
    else:
        sum_of_missing_numbers = sum(missing_numbers)
        if sum_of_missing_numbers % 2:
            return bin(sum_of_missing_numbers)[2:]
        else:
            return hex(sum_of_missing_numbers)[2:]