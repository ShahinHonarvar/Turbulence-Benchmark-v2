def return_binary_or_hexa(tup):
    a = tup[68]
    b = tup[99]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in tup[69:99]:
            total_sum += i
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]