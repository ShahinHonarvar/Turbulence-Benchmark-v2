def return_binary_or_hexa(numbers):
    if len(numbers) <= 88:
        return ''
    a = numbers[56]
    b = numbers[88]
    sum_value = sum((i for i in range(a + 1, b) if i not in numbers[57:88]))
    if sum_value == 0:
        return ''
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]