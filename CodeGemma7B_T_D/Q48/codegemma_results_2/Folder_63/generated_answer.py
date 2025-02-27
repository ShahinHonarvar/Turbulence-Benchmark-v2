def return_binary_or_hexa(tuple):
    a = tuple[81]
    b = tuple[86]
    excluded_numbers = set(range(a + 1, b))
    excluded_numbers.difference_update(tuple[81:87])
    sum_of_excluded_numbers = sum(excluded_numbers)
    if sum_of_excluded_numbers % 2 == 1:
        return bin(sum_of_excluded_numbers)[2:]
    else:
        return hex(sum_of_excluded_numbers)[2:].upper()