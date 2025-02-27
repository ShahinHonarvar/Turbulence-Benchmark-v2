def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    total_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in t[4:9] if a < i < b))
    diff = total_sum - actual_sum
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]