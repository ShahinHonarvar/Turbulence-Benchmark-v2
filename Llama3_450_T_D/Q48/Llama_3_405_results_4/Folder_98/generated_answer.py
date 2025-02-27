def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    total = sum((i for i in range(a + 1, b) if i not in numbers[7:]))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]