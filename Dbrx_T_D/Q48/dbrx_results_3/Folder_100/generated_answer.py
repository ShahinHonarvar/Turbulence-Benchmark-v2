def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[44]
    b = numbers_tuple[78]
    sum_of_missing_numbers = 0
    for num in range(a + 1, b):
        if num not in numbers_tuple[44:79]:
            sum_of_missing_numbers += num
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'x')