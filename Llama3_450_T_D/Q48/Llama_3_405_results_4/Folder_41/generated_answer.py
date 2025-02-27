def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    total_sum = sum(range(a + 1, b))
    existing_sum = sum((x for x in t[4:8] if a < x < b))
    diff_sum = total_sum - existing_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 != 0:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]