def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[4])
    missing_numbers = set(range(a + 1, b)) - set(numbers[1:4])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''