def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    present_numbers = set(numbers[49:76])
    missing_numbers = {num for num in range(a + 1, b) if num not in present_numbers}
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]