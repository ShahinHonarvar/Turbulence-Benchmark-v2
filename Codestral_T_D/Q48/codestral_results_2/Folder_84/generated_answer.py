def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[32 + 1:44]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    return ''