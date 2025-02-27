def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    sum_val = sum((i for i in range(a + 1, b) if i not in numbers[20:52]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]