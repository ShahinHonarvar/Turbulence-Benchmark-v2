def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    numbers_in_range = set(numbers[39:81])
    sum_missing = sum((num for num in range(a + 1, b) if num not in numbers_in_range))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return format(sum_missing, 'X')
    else:
        return format(sum_missing, 'b')