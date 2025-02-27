def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    total_sum = sum((i for i in range(a + 1, b) if i not in t))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]