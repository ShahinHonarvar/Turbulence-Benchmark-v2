def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    total = sum((i for i in range(a + 1, b) if i not in numbers[36:52]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]