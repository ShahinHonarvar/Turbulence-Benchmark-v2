def return_binary_or_hexa(tup):
    a, b = (tup[80], tup[200])
    sum = 0
    for x in range(a + 1, b):
        if x not in tup[80:200]:
            sum += x
    return bin(sum)[2:] if sum % 2 else hex(sum).upper()[2:]