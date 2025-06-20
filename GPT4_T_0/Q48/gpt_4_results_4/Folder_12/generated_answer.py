def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    missing_numbers = set(range(a + 1, b)) - set(numbers[16:88])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ''
    elif sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()