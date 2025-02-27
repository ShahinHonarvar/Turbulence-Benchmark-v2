def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[88]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[56:89]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]