def return_binary_or_hexa(num_tuple):
    num_tuple.sort()
    a = num_tuple[13]
    b = num_tuple[35]
    sum = 0
    for i in range(a + 1, b):
        if i not in num_tuple[13:36]:
            sum += i
    if sum % 2 == 1:
        return str(bin(sum))[2:]
    else:
        return hex(sum)[2:].upper()