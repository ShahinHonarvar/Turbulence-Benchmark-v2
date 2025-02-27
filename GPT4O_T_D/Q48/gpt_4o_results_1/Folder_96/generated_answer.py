def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    sum_value = sum((x for x in range(a + 1, b) if x not in numbers[51:200]))
    if sum_value == 0:
        return ''
    if sum_value % 2:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]