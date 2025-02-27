def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[86]
    b = numbers_tuple[99]
    present_numbers = set(numbers_tuple[86:100])
    sum_of_missing_numbers = sum((i for i in range(a, b + 1) if i not in present_numbers))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()