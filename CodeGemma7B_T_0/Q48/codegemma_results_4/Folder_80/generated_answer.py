def return_binary_or_hexa(tupl):
    a, b = (tupl[57], tupl[84])
    sum = 0
    for i in range(a + 1, b):
        if i not in tupl[57:85]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()