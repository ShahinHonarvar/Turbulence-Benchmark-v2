def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    present_numbers = set(numbers[276:871])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]