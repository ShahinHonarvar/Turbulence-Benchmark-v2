def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[93]
    sum = 0
    for i in range(a + 1, b):
        if i not in input_tuple[20:94]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()