def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[80]
    b = numbers_tuple[200]
    sum_of_missing_numbers = sum((x for x in range(a + 1, b) if x not in numbers_tuple[80:201]))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()