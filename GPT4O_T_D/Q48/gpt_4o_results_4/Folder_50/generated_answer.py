def return_binary_or_hexa(numbers):
    if len(numbers) <= 76:
        return ''
    a = numbers[13]
    b = numbers[76]
    present_numbers = set(numbers[14:76])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')