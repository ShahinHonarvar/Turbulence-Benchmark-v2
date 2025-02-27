def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    total = sum((i for i in range(a + 1, b) if i not in numbers[34:70]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]