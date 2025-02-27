def return_binary_or_hexa(*args):
    n = 78
    summa = 0
    for i in range(n):
        summa += i + args[44] + 1
    if summa % 2:
        return bin(summa)[2:]
    else:
        return hex(summa)[2:].upper()