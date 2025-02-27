def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:29])
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]