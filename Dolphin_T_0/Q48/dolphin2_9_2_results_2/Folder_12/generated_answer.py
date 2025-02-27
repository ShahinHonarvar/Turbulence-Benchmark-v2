def return_binary_or_hexa(integers):
    a = integers[16]
    b = integers[87]
    sum = 0
    for i in range(a + 1, b):
        if i not in integers:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]