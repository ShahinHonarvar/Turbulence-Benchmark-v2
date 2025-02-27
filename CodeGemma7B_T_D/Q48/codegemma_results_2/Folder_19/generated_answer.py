def return_binary_or_hexa(tuple):
    a = tuple[1]
    b = tuple[4]
    summation = 0
    for i in range(a + 1, b):
        if i not in tuple[1:4]:
            summation += i
    return bin(summation)[2:] if summation % 2 else hex(summation)[2:].upper()