def return_binary_or_hexa(numbers):
    a, _, b = numbers
    total = sum((i for i in range(a + 1, b) if i not in numbers))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]