def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[2]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers[1:3]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]