def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    total_sum = sum(range(a + 1, b))
    tuple_sum = sum((x for x in t[1:10] if a < x < b))
    diff = total_sum - tuple_sum
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]