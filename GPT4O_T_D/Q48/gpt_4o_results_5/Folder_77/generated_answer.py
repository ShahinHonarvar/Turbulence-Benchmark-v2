def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers[19:52]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')