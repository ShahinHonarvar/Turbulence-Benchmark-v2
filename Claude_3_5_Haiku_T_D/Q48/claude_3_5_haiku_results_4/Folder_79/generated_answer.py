def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    exclude_set = set(tup[1:8])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in exclude_set:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]