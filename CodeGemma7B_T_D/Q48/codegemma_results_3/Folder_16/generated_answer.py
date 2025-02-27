def return_binary_or_hexa(tup):
    sum = 0
    a = tup[90]
    b = tup[97]
    for i in range(a + 1, b):
        if i not in tup[90:98]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].lower()