def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[14:36]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]