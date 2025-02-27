def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[2]
    sum_of_missing = 0
    for num in range(a + 1, b):
        if num not in numbers[:3]:
            sum_of_missing += num
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]