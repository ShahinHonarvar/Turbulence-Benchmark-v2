def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    num_set = set(numbers[12:76])
    sum_missing = sum((num for num in range(a + 1, b) if num not in num_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return format(sum_missing, 'X')
    else:
        return format(sum_missing, 'b')