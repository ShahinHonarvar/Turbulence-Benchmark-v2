def return_binary_or_hexa(numbers):
    a, b = (numbers[1], numbers[7])
    missing_nums_sum = sum((x for x in range(a + 1, b) if x not in numbers[2:7]))
    if missing_nums_sum == 0:
        return ''
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]