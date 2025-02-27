def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    if all((x in numbers for x in range(a + 1, b))):
        return ''
    missing = [x for x in range(a + 1, b) if x not in numbers]
    sum_missing = sum(missing)
    result = ''
    if sum_missing % 2 == 0:
        result = hex(sum_missing)[2:]
    else:
        result = bin(sum_missing)[2:]
    return result