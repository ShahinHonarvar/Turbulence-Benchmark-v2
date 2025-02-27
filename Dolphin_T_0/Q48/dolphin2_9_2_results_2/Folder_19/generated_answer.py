def return_binary_or_hexa(tupl):
    a = tupl[1]
    b = tupl[4]
    total = sum((val for val in range(a + 1, b) if val not in tupl[1:4]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]