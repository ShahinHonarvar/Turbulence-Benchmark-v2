def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    if a + 1 == b - 1:
        return ''
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[50:74]))
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')