def return_binary_or_hexa(args):
    total = 0
    for i in range(args[20] + 1, args[36] + 1):
        if i not in args[20:37]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()