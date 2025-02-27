def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    number_set = set(numbers[276:871])
    missing_sum = sum((x for x in range(a + 1, b) if x not in number_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]