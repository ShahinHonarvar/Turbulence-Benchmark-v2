def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[87:99])
    missing_numbers.difference_update(present_numbers)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')