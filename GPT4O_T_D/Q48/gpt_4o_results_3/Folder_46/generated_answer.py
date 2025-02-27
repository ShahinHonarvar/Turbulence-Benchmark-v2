def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    sum_absent = sum((i for i in range(a + 1, b) if i not in numbers[11:79]))
    if sum_absent == 0:
        return ''
    if sum_absent % 2 == 0:
        return format(sum_absent, 'X')
    else:
        return format(sum_absent, 'b')