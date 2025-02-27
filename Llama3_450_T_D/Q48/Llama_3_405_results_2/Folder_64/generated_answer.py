def return_binary_or_hexa(t):
    a, _, _, _, _, b = t
    total_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t))
    diff = total_sum - actual_sum
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]