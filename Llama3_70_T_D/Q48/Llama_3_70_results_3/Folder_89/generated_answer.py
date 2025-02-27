def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    numbers = set(range(a + 1, b)) - set(t[55:85])
    if not numbers:
        return ''
    total = sum(numbers)
    return bin(total)[2:] if total % 2 else hex(total)[2:]