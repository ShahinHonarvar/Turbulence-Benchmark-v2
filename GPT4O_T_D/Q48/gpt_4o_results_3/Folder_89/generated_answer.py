def return_binary_or_hexa(numbers):
    if len(numbers) < 85 or numbers[84] <= numbers[55] + 1:
        return ''
    a = numbers[55]
    b = numbers[84]
    numbers_between = set(numbers[56:84])
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers_between))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        hexa = hex(sum_missing)[2:]
        return hexa
    else:
        binary = bin(sum_missing)[2:]
        return binary