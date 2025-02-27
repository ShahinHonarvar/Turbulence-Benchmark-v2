def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[10:101]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')