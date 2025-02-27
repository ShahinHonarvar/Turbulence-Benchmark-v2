def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    sum_range = sum((x for x in range(a + 1, b) if x not in numbers[34:78]))
    if sum_range == 0:
        return ''
    if sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]