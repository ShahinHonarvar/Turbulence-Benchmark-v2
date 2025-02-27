def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[5]
    total = sum((i for i in range(a + 1, b) if i not in numbers[:6]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]