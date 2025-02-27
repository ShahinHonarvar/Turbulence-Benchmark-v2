def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[11:77]:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]