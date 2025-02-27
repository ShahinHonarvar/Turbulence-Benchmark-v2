def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[110:348]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]