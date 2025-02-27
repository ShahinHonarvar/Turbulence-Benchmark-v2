def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    total = sum((i for i in range(a + 1, b) if i not in numbers[29:53]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]