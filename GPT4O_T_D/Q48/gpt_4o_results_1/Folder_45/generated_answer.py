def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a = numbers[30]
    b = numbers[200]
    numbers_in_range = set(numbers[31:200])
    sum_missing = sum((x for x in range(a + 1, b) if x not in numbers_in_range))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]