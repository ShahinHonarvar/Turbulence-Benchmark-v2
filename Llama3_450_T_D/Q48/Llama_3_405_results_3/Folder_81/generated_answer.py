def return_binary_or_hexa(t):
    a = t[10]
    b = t[100]
    s = set(t[10:101])
    total_sum = sum((i for i in range(a + 1, b) if i not in s))
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]