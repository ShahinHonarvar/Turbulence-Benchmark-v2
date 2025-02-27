def return_binary_or_hexa(tuple):
    sum = 0
    for i in range(47, 92):
        if i not in tuple and i > tuple[46] and (i < tuple[91]):
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]