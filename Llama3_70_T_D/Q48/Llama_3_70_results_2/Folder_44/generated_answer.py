def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[52])
    numbers = set(tup[36:53])
    total = sum((i for i in range(a + 1, b) if i not in numbers))
    return bin(total)[2:] if total % 2 else hex(total)[2:]