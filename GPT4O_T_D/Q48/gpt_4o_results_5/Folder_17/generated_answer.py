def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[74:84])
    missing_numbers = full_range - present_numbers
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]