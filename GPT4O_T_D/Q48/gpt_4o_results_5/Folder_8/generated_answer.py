def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    numbers_set = set(numbers[46:48])
    sum_integers = sum((x for x in range(a + 1, b) if x not in numbers_set))
    if sum_integers == 0:
        return ''
    if sum_integers % 2:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:]