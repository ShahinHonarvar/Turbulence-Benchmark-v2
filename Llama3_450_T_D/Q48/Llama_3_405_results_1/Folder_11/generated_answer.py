def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    total = sum((i for i in range(a + 1, b) if i not in numbers[49:76]))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]