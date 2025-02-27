def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    if set(range(a + 1, b)) <= set(numbers[86:89]):
        return ''
    sum_integers = sum((i for i in range(a + 1, b) if i not in numbers[86:89]))
    if sum_integers % 2 == 1:
        return '{bin(sum_integers)[2:]}'
    else:
        return '{hex(sum_integers)[2:]}'