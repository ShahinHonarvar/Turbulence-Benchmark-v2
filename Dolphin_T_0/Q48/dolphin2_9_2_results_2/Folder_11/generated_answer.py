def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    missing = [x for x in range(a + 1, b) if x not in numbers]
    sum_missing = sum(missing)
    if all((i in numbers for i in range(a + 1, b))):
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]