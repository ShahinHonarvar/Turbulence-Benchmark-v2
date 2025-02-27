def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    total = sum((i for i in range(a + 1, b) if i not in numbers[20:201]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]