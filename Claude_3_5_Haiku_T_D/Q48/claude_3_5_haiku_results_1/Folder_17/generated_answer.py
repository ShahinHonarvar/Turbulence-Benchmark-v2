def return_binary_or_hexa(tup):
    a = tup[73]
    b = tup[84]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in tup[73:85]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]