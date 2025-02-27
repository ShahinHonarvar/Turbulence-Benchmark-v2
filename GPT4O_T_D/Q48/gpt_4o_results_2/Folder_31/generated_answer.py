def return_binary_or_hexa(numbers):
    a, b = (numbers[33], numbers[78])
    missing_sum = sum((n for n in range(a + 1, b) if n not in set(numbers[34:78])))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]