def return_binary_or_hexa(args):
    a = args[36]
    b = args[85]
    sum = 0
    for i in range(a + 1, b):
        if i not in args:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper() if b - a > 2 else ''
    else:
        return bin(sum)[2:] if b - a > 2 else ''