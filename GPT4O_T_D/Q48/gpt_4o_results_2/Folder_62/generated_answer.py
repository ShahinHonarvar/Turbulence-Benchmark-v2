def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    numbers_in_range = set(numbers[51:92])
    sum_value = sum((x for x in range(a + 1, b) if x not in numbers_in_range))
    if sum_value == 0:
        return ''
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]