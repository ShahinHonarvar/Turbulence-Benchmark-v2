def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[200:203]:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return hex(sum)[2:]