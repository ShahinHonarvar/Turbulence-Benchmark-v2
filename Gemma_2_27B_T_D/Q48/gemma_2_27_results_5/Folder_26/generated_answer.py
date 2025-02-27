def return_binary_or_hexa(input_tuple):
    a = input_tuple[68]
    b = input_tuple[99]
    total = 0
    for i in range(a + 1, b):
        if i not in input_tuple[68:99 + 1]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]