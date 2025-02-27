def return_binary_or_hexa(numbers):
    a, *_, b = numbers
    total = sum((i for i in range(a + 1, b) if i not in numbers))
    return bin(total)[2:] if total % 2 else hex(total)[2:]