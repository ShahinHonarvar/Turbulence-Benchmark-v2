def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    sum_missing = 0
    numbers_set = set(numbers[38:43])
    for num in range(a + 1, b):
        if num not in numbers_set:
            sum_missing += num
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]