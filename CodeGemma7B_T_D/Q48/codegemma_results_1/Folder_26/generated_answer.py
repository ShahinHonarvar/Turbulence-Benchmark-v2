def return_binary_or_hexa(tuple):
    a = tuple[68]
    b = tuple[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple[68:100]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()