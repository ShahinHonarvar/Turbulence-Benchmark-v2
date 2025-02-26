def return_binary_or_hexa(tup):
    a = tup[933]
    b = tup[996]
    present_set = set(tup[933:997])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present_set:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum > 0:
        return hex(total_sum)[2:]
    else:
        return ''