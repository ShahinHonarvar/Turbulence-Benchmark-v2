def return_binary_or_hexa(numbers):
    if len(numbers) < 85:
        return ''
    a = numbers[57]
    b = numbers[84]
    required_set = {i for i in range(a + 1, b)}
    present_set = set(numbers[58:84])
    missing_numbers = required_set - present_set
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]