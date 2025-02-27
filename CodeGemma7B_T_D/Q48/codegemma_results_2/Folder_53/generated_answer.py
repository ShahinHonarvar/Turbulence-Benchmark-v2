def return_binary_or_hexa(tuples):
    a, b = (tuples[200], tuples[202])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuples:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()