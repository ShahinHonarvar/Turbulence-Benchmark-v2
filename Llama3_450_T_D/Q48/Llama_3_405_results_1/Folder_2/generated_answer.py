def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    total = sum((i for i in range(a + 1, b) if i not in numbers[73:93]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]