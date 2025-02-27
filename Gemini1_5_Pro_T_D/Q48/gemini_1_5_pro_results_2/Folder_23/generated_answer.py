def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[36]
    sum = 0
    for num in range(a + 1, b):
        if num not in tup[20:37]:
            sum += num
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]