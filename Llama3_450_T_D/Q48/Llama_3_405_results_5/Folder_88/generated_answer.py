def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[9]
    total = sum((i for i in range(a + 1, b) if i not in numbers[4:9]))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]