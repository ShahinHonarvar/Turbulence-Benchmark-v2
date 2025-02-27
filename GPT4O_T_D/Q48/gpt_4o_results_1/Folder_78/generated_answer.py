def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    numbers_set = set(numbers[63:96])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]