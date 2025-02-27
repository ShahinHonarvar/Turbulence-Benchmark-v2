def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[97]
    total_sum = sum(range(a + 1, b))
    tup_sum = sum((i for i in tup[11:97] if a < i < b))
    diff_sum = total_sum - tup_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 == 1:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]