def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    numbers_set = set(numbers[81:200])
    total = 0
    for num in range(a + 1, b):
        if num not in numbers_set:
            total += num
    if total == 0:
        return ''
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')