def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[11:79]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x').lstrip('0')
    else:
        return format(missing_sum, 'b').lstrip('0')