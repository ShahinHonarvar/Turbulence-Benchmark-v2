def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[10:80]:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return format(sum, 'x')