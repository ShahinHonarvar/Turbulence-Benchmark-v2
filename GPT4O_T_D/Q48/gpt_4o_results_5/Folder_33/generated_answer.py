def return_binary_or_hexa(numbers):
    if len(numbers) <= 35:
        return ''
    a = numbers[13]
    b = numbers[35]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers[14:35]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]