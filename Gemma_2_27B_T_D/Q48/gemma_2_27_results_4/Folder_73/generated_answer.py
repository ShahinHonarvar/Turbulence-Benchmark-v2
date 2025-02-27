def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[10:77]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]