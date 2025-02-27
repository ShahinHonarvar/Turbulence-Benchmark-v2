def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    missing_numbers = set(range(a + 1, b)).difference(numbers[11:29])
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]