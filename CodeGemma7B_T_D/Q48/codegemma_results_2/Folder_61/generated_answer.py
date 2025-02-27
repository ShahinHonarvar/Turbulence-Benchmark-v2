def return_binary_or_hexa(*args):
    args = sorted(args)
    a, b = (args[0], args[8])
    sum = 0
    for i in range(a + 1, b):
        if i not in args:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].upper()