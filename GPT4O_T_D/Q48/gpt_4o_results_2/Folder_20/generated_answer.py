def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    missing_numbers = set(range(a + 1, b)).difference(numbers[28:96])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]