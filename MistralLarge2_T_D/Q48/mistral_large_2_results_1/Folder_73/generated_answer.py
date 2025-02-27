def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[76])
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers[10:77]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]