def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[19:60]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]