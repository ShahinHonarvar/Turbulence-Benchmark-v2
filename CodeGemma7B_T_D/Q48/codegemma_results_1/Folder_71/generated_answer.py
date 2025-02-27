def return_binary_or_hexa(args):
    sum = 0
    for i in range(args[20] + 1, args[35] + 1):
        if not i in args:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()