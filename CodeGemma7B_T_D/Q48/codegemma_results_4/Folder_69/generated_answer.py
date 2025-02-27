def return_binary_or_hexa(a, b, tuple):
    sum = 0
    for integer in tuple:
        if integer > a and integer < b:
            pass
        else:
            sum += integer
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]