def return_binary_or_hexa(args):
    a = args[13]
    b = args[76]
    if a >= b:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in args[13:77]:
            sum += i
    if sum % 2 == 0:
        return hex(sum).split('x')[-1].upper()
    else:
        return bin(sum).split('b')[-1]