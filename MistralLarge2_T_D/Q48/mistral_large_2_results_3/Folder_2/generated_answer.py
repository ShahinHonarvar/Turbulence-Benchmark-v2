def return_binary_or_hexa(numbers):
    a, b = (numbers[72], numbers[93])
    present_numbers = set(numbers[72:94])
    missing_sum = sum((n for n in range(a + 1, b) if n not in present_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()