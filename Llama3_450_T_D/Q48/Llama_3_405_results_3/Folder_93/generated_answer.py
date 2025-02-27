def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    total = sum((i for i in range(a + 1, b) if i not in numbers[58:85]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]