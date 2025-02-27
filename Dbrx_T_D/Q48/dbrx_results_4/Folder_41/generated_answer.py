def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[8]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[3:9]:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return hex(sum)[2:].upper()