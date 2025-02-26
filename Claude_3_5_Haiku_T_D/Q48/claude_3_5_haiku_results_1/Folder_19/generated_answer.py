def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in tup[1:5]:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]