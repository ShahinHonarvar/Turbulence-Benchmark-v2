def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    total_sum = 0
    num_set = set(numbers[39:44])
    for i in range(a + 1, b):
        if i not in num_set:
            total_sum += i
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')