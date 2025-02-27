def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers:
            total += i
    if total % 2 == 0:
        result = hex(total)[2:]
    else:
        result = bin(total)[2:]
    return result