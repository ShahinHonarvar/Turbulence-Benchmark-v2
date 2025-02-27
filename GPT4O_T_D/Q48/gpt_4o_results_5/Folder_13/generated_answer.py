def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    numbers_set = set(numbers[47:91])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]