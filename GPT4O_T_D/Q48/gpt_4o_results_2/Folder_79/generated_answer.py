def return_binary_or_hexa(numbers):
    a, b = (numbers[1], numbers[7])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[2:7]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]