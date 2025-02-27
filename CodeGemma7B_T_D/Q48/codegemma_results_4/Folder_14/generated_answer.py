def return_binary_or_hexa(tupl):
    a = tupl[2]
    b = tupl[5]
    toret = 0
    for i in range(a + 1, b):
        if i not in tupl[2:6]:
            toret += i
    if toret & 1 == 1:
        return bin(toret)[2:]
    else:
        return hex(toret)[2:]