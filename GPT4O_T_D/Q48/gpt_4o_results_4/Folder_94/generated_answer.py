def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    absent_sum = 0
    found = set(numbers[43:87])
    for num in range(a + 1, b):
        if num not in found:
            absent_sum += num
    if absent_sum == 0:
        return ''
    if absent_sum % 2 == 0:
        return format(absent_sum, 'x')
    else:
        return format(absent_sum, 'b')