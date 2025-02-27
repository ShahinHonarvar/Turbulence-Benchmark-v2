def return_binary_or_hexa(numbers):
    a, b = (numbers[35], numbers[64])
    present_numbers = set(numbers[36:64])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:] if missing_sum else ''