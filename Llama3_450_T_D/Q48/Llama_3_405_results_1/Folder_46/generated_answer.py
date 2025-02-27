def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    total = sum((i for i in range(a + 1, b) if i not in numbers[11:79]))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]