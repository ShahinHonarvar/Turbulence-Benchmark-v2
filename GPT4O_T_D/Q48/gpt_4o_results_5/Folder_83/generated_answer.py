def return_binary_or_hexa(numbers):
    a_index = 90
    b_index = 200
    if len(numbers) <= b_index or a_index >= b_index:
        return ''
    a = numbers[a_index]
    b = numbers[b_index]
    present_numbers = set(numbers[a_index + 1:b_index])
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]