def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    total_sum = sum(range(a + 1, b))
    tuple_sum = sum((i for i in t[2:7] if a < i < b))
    diff = total_sum - tuple_sum
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]