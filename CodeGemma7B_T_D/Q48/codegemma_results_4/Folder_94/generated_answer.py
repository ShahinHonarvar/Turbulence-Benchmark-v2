def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    summation = 0
    for num in range(a + 1, b):
        if num not in tup[42:88]:
            summation += num
    if summation % 2:
        binary_rep = bin(summation)[2:]
        return binary_rep
    else:
        hexa_rep = hex(summation)[2:].upper()
        return hexa_rep