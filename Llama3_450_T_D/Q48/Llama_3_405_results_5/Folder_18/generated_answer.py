def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    total_sum = sum(range(a + 1, b))
    tuple_sum = sum((i for i in t[57:90] if a < i < b))
    diff = total_sum - tuple_sum
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]