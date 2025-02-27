def return_binary_or_hexa(tple):
    a, b, *_ = tple[6:10]
    binary = hexadecimal = 0
    for x in range(a + 1, b):
        if x not in tple[6:10]:
            if x % 2:
                binary += x
            else:
                hexadecimal += x
    return bin(binary)[2:] or hex(hexadecimal)[2:].upper()