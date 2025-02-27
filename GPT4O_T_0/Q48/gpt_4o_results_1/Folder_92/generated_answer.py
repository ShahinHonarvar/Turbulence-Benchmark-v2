def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[2]
    sum_of_missing = sum((x for x in range(a + 1, b) if x not in numbers[1:3]))
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]