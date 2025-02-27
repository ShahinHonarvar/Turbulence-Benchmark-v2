def return_binary_or_hexa(tup):
    sum = 0
    a = tup[40] + 1
    b = tup[200] - 1
    for integer in range(a, b + 1):
        if integer not in tup[40:200]:
            sum += integer
    if sum & 1 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()