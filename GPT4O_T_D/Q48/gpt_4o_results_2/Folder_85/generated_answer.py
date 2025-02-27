def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    sum_missing = sum((num for num in range(a + 1, b) if num not in numbers[2:8]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]