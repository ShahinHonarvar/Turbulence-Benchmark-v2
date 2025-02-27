def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    total_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t[933:997]))
    diff_sum = total_sum - actual_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 != 0:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]