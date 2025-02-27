def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in numbers[45:79]))
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2 == 1:
        return f'{sum_of_missing:b}'
    else:
        return f'{sum_of_missing:x}'