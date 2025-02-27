def return_binary_or_hexa(*args):
    a = args[17]
    b = args[88]
    sum = 0
    for i in range(a + 1, b):
        if i not in args:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].upper() if sum >= 16 else hex(sum)[2:]