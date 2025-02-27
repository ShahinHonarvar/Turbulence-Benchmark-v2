def return_binary_or_hexa(numbers):
    a, b = (numbers[37], numbers[43])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[37 + 1:43]))
    return bin(missing_sum).lstrip('0b') if missing_sum % 2 else hex(missing_sum).lstrip('0x')