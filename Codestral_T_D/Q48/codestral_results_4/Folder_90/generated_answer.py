def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    missing_numbers = set(range(a + 1, b)) - set(numbers[60:91])
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]