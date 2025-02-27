def return_binary_or_hexa(input_tuple):
    a = input_tuple[6]
    b = input_tuple[7]
    total = 0
    for i in range(a + 1, b):
        if i not in input_tuple[6:8]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]