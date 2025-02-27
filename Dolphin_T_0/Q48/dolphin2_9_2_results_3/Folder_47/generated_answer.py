def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]