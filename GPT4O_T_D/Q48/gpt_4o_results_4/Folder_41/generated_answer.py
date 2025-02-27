def return_binary_or_hexa(numbers):
    if len(numbers) < 9:
        return ''
    a = numbers[3]
    b = numbers[8]
    sum_missing = 0
    for num in range(a + 1, b):
        if num not in numbers[3:9]:
            sum_missing += num
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]