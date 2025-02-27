def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    internal_range = set(range(a + 1, b))
    present_numbers = set(numbers[934:996])
    missing_sum = sum(internal_range - present_numbers)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]