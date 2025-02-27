def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    total = sum((i for i in range(a + 1, b) if i not in numbers[0:5]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]