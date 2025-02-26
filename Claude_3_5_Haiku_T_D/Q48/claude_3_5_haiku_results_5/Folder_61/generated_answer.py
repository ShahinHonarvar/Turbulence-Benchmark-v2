def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    present = set(t[0:9])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]