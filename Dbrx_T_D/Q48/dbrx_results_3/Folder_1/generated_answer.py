def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return format(sum, 'x')