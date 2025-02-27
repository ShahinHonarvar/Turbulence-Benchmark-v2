def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[29:54]:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]