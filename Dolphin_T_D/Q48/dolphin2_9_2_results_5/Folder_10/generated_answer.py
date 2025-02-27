def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    total = sum((i for i in range(a + 1, b) if i not in numbers[36:55]))
    if total % 2 == 1:
        return bin(total)[2:]
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return ''