def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    total = sum((i for i in range(a + 1, b) if i not in numbers[32:100]))
    return bin(total)[2:] if total & 1 else hex(total)[2:]