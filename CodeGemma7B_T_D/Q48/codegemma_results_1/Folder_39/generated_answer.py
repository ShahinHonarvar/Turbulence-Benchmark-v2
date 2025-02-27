def return_binary_or_hexa(tuple):
    if tuple[91] - tuple[44] <= 47:
        return ''
    sum = 0
    for i in range(tuple[44] + 1, tuple[91]):
        if i not in tuple:
            sum += i
    if sum % 2 != 0:
        return str(bin(sum))[2:]
    else:
        return str(hex(sum))[2:].upper()