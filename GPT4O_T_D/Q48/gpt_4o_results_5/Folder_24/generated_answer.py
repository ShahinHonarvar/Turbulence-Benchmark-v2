def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    numbers_set = set(numbers[14:91])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]