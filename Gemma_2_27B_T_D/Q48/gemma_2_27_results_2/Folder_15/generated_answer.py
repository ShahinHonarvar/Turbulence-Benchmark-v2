def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    total = sum([i for i in range(a + 1, b) if i not in numbers])
    if total % 2 != 0:
        return bin(total)[2:]
    return hex(total)[2:].lower()