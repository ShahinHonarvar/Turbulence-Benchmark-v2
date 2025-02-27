def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[8:9]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]