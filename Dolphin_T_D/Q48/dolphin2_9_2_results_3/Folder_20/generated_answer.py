def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[27:97]]
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()