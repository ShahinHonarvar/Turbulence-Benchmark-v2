def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[12])
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:13])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''