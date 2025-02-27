def return_binary_or_hexa(tuples):
    a = tuples[20]
    b = tuples[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuples[20:44]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]