def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in tup[111:348]))
    diff = expected_sum - actual_sum
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]