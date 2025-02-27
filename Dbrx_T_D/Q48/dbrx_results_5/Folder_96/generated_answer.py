def return_binary_or_hexa(args):
    a = args[50]
    b = args[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in args[50:201]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()