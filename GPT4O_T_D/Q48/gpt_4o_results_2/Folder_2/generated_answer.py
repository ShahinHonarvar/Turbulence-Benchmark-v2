def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    between_ab_set = set(range(a + 1, b))
    missing_numbers = sorted(between_ab_set - set(numbers[73:93]))
    if not missing_numbers:
        return ''
    result_sum = sum(missing_numbers)
    if result_sum % 2 == 1:
        return bin(result_sum)[2:]
    else:
        return hex(result_sum)[2:]