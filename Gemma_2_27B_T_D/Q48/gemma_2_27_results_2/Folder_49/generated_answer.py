def return_binary_or_hexa(input_tuple):
    a = input_tuple[80]
    b = input_tuple[200]
    total = 0
    for i in range(a + 1, b):
        if i not in input_tuple[80:201]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]