def return_binary_or_hexa(tuple):
    sum = 0
    for i in range(tuple[200] + 1, tuple[202]):
        if i not in tuple[200:203]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]