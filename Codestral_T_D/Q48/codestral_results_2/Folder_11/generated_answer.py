def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    missing_numbers = set(range(a + 1, b)) - set(numbers[48:76])
    total_sum = sum(missing_numbers)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]