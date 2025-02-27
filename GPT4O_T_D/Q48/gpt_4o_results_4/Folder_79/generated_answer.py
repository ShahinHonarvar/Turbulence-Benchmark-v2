def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[1:8]))
    if missing_sum == 0:
        return ''
    return format(missing_sum, 'b') if missing_sum % 2 != 0 else format(missing_sum, 'x')